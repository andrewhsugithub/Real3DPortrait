from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from inference.real3d_infer import GeneFace2Infer

from server.dto import Real3DRequest

import os

router = APIRouter()

@router.post("/real3d/")
async def real3d(req: Real3DRequest) -> FileResponse:
    args = req.copy(deep=True)
    inp = {
        'a2m_ckpt': args.a2m_ckpt,
        'head_ckpt': args.head_ckpt,
        'torso_ckpt': args.torso_ckpt,
        'src_image_name': args.src_img,
        'bg_image_name': args.bg_img,
        'drv_audio_name': args.drv_aud,
        'drv_pose_name': args.drv_pose,
        'blink_mode': args.blink_mode,
        'temperature': args.temperature,
        'mouth_amp': args.mouth_amp,
        'out_name': args.out_name,
        'out_mode': args.out_mode,
        'map_to_init_pose': args.map_to_init_pose,
        'head_torso_threshold': args.head_torso_threshold,
        'seed': args.seed,
        'min_face_area_percent': args.min_face_area_percent,
        'low_memory_usage': args.low_memory_usage,
        }

    GeneFace2Infer.example_run(inp)
    
    # vid_path = osp.join(args.output_dir, f'{basename(args.source)}--{basename(args.driving)}.mp4')
    vid_path = 'infer_out/tmp/' + os.path.basename(inp['src_image_name'])[:-4] + '_' + os.path.basename(inp['drv_pose_name'])[:-4] + '.mp4' if inp['out_name'] == '' else inp['out_name']
        
    response = FileResponse(vid_path)

    return response