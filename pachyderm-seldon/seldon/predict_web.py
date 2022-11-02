import sys
from skimage import io
import matplotlib.pyplot as plt
from seldon_core.seldon_client import SeldonClient
import gradio as gr

def dog_or_cat(image):
    seldon_ip = "10.10.160.183"
    sc = SeldonClient(deployment_name="kt-deploy-update", namespace="seldon", gateway_endpoint=f"{seldon_ip}", gateway="istio")
    out = sc.predict(transport="rest", data=image)
    res = out.response['data']['ndarray'][0]
    return res

demo = gr.Interface(fn=dog_or_cat, inputs="image", outputs="text", examples=["Yogi.png","Zoey.png","cat.png"])
demo.launch(share=True)