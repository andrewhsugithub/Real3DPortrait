from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from inference.real3d_infer import GeneFace2Infer

from server.dto import Real3DRequest

import datetime

import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Function to read public key from a PEM file and return it as a byte string
def load_public_key_pem(pem_file_path):
    # Read the PEM file
    with open(pem_file_path, 'rb') as pem_file:
        pem_data = pem_file.read()
    
    # Load the public key
    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

    # Return the public key in PEM format as a byte string
    return public_key

# Example usage
pem_file_path = 'keys/jwtRSA256-public.pem'  # Specify the path to your PEM file
public_key = load_public_key_pem(pem_file_path)

router = APIRouter()

@router.post("/real3d/")
async def real3d(req: Real3DRequest, request: Request) -> FileResponse:
    try:
        access_token = request.headers['Authorization'].split(' ')[1]
        payload = jwt.decode(access_token, public_key, algorithms=["RS256"])
    except jwt.exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token has expired"}, status_code=401)
        
    user_id = req.user_id
    emotion = req.emotion
    filename = req.drv_aud.split('/')[-1][:-4]
    
    args = req.copy(deep=True)
    #! should not be hard coded here
    inp = {
        'a2m_ckpt': args.a2m_ckpt,
        'head_ckpt': args.head_ckpt,
        'torso_ckpt': args.torso_ckpt,
        # 'src_image_name': f"/mnt/Nami/users/Jason0411202/buckets/{user_id}/image/{emotion}/{emotion}.png",
        'src_image_name': args.src_img,
        'bg_image_name': args.bg_img,
        'drv_audio_name': args.drv_aud,
        'drv_pose_name': args.drv_pose,
        'blink_mode': args.blink_mode,
        'temperature': args.temperature,
        'mouth_amp': args.mouth_amp,
        'out_name': f"/mnt/Nami/users/Jason0411202/buckets/{user_id}/Real3D/{filename}.mp4",
        'out_name': args.out_name,
        'out_mode': args.out_mode,
        'map_to_init_pose': args.map_to_init_pose,
        'head_torso_threshold': args.head_torso_threshold,
        'seed': args.seed,
        'min_face_area_percent': args.min_face_area_percent,
        'low_memory_usage': args.low_memory_usage,
        }
    
    # date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # inp['out_name'] = f"/mnt/Nami/users/Jason0411202/buckets/{user_id}/Real3D/{date}.mp4"

    GeneFace2Infer.example_run(inp)
    
    vid_path = inp['out_name']
        
    response = FileResponse(vid_path)

    return vid_path