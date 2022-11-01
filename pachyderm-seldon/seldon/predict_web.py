import sys
from skimage import io
import matplotlib.pyplot as plt
from seldon_core.seldon_client import SeldonClient

""""
if __name__ == '__main__':
    seldon_ip = sys.argv[1]
    image = io.imread("dog.png")

    sc = SeldonClient(deployment_name="dogcat-deploy", namespace="seldon", gateway_endpoint=f"{seldon_ip}:80", gateway="istio")
    out = sc.predict(transport="rest", data=image)

    if out.success:
        res = out.response['data']['ndarray'][0]
        plt.imshow(image)
        plt.title(f"Prediction: {res}")
        plt.show()
"""

# Psuedo-code - Kate
def dog_or_cat(image):
    seldon_ip = sys.argv[1]
    #we don't need io.imread("imagefile.png") because we already have an image and should be able to just use it
    sc = SeldonClient(deployment_name="dogcat-deploy", namespace="seldon", gateway_endpoint=f"{seldon_ip}:80", gateway="istio")
    out = sc.predict(transport="rest", data=image)
    # if out.success: ## Not sure we need this, Gradio usually handles errors...
    res = out.response['data']['ndarray'][0]
    plt.imshow(image)
    plt.title(f"Prediction: {res}")
    plt.show()

if __name__ == '__main__':
    demo = gr.Interface(fn=dog_or_cat, inputs="image", outputs="image")
    demo.launch()