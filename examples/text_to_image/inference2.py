from diffusers import StableDiffusionPipeline
import torch

model_path = "sd-pokemon-model-lora"
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
#pipe.unet.load_attn_procs(model_path)
pipe.to("cuda")

prompt = "Feed-Forward Neural Network Backpropagation"
image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
image.save("untrained_backprop.png")
