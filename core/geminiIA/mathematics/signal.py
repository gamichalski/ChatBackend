from .models import MathAI
from django.db.models.signals import post_save
from django.dispatch import receiver
import google.generativeai as genai
import mimetypes
from .config_ia import model

@receiver(post_save, sender=MathAI)
def SendResponse(instance, sender, created, **kwargs):
    if created:
        try: 
            image_path = instance.cover.path if instance.cover else None
            if image_path:
                file_type = mimetypes.guess_type(image_path)
                myfile = genai.upload_file(str(instance.cover), mime_type=str(file_type[0]))

                if myfile and instance.answer:
                    content = model.generate_content([myfile, instance.answer])
                    instance.response = content.candidates[0].content.parts[0].text
                else:
                    content = model.generate_content([myfile, ""])
                    instance.response = content.candidates[0].content.parts[0].text
                myfile.delete()
            else:
                content = model.generate_content([instance.answer])
                instance.response = content.candidates[0].content.parts[0].text
            
            instance.save()
        except Exception as e:
            instance.response = f"ERRO: {str(e)}"
            instance.save()