from rest_framework.decorators import api_view
from django.http import JsonResponse
from apkid.apkid import Scanner,Options
import subprocess
from app import models
import os
from apkChecker.settings import BASE_DIR
# Create your views here.
@api_view(["GET"])
def function(request):
    try:
        apk = request.FILES["apk"]
        models.File.objects.create(fileName=apk)
    except Exception as e:
        return JsonResponse({"message":"Please Provide a dex or a apk file"},status=403)
    filePath = os.path.join(BASE_DIR,"files\\"+apk.name)
    data = subprocess.run(["apkid",filePath],capture_output=True)
    try:
        os.remove(filePath)
    except:
        print("something Error happened")
    #except Exception as e:
        #print(e)
        #return JsonResponse({"message":"Please Provide a valid apk or dex"},status=403)
    final_output = data.stdout.decode("utf-8")
    return JsonResponse({"message":final_output})