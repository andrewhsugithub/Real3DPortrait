from pydantic import BaseModel, Field
from typing import Literal, Optional
from enum import Enum

class BlinkModeEnum(str, Enum):
    none = "none"
    period = "period"

class OutModeEnum(str, Enum):
    final = "final"
    concat_debug = "concat_debug"

class Real3DRequest(BaseModel):
    a2m_ckpt: Optional[str] = Field(default='checkpoints/240210_real3dportrait_orig/audio2secc_vae', description='Path to A2M checkpoint')
    head_ckpt: Optional[str] = Field(default='', description='Path to head checkpoint')
    torso_ckpt: Optional[str] = Field(default='checkpoints/240210_real3dportrait_orig/secc2plane_torso_orig', description='Path to torso checkpoint')
    ############### Input Args ################# 
    src_img: Optional[str] = Field(default='data/raw/examples/Macron.png', description='Path to source image')
    bg_img: Optional[str] = Field(default='', description='Path to background image')
    drv_aud: Optional[str] = Field(default='data/raw/examples/Obama_5s.wav', description='Path to driving audio file')
    drv_pose: Optional[str] = Field(default='data/raw/examples/May_5s.mp4', description='Path to driving pose video')
    blink_mode: Optional[BlinkModeEnum] = Field(default=BlinkModeEnum.period, description='Blink mode: none or period')
    temperature: Optional[float] = Field(default=0.2, description='sampling temperature in audio2motion, higher -> more diverse, less accurate')
    mouth_amp: Optional[float] = Field(default=0.45, description='scale of predicted mouth, enabled in audio-driven')
    head_torso_threshold: Optional[float] = Field(default=None, description="0.1~1.0, turn up this value if the hair is translucent")
    out_name: Optional[str] = Field(default='', description='Output filename')
    out_mode: Optional[OutModeEnum] = Field(default=OutModeEnum.concat_debug, description='final: only output talking head video; concat_debug: talking head with internel features')
    map_to_init_pose: bool = Field(default=True, description='Whether to map the pose of the first frame to source image')
    seed: Optional[int] = Field(default=None, description='random seed, default None to use time.time()')
    min_face_area_percent: Optional[float] = Field(default=0.2, description='scale of predicted mouth, enabled in audio-driven')
    low_memory_usage: bool = Field(default=False, description='write img to video upon generated, leads to slower fps, but use less memory')