from .models import TextWritingAI
from django.db.models.signals import post_save
from django.dispatch import receiver
import mimetypes
import google.generativeai as genai
from .config_ia import model, response
from core.chat.models import Answer, Chat

@receiver(post_save, sender=TextWritingAI)
def SendResponse(instance, sender, created, **kwargs):
    if created:
        try: 
            image_path = instance.cover.path if instance.cover else None
            if image_path:
                file_type = mimetypes.guess_type(image_path)
                myfile = genai.upload_file(str(instance.cover), mime_type=str(file_type[0]))

                if myfile and instance.answer:
                    content = model.generate_content([myfile, instance.answer])
                    instance.response = content.text
                else:
                    content = model.generate_content([myfile, ""])
                    instance.response = content.text
                myfile.delete()
            else:
                content = response.send_message(instance.answer)
                instance.response = content.text
                chat, created = Chat.objects.get_or_create(chat_name=instance.answer, defaults={"user": instance.user, "ia": 5})
                answer = Answer.objects.create(chat=chat, answer=instance.answer, response=instance.response)
            
            instance.save()
        except Exception as e:
            instance.response = f"ERRO: {str(e)}"
            instance.save()