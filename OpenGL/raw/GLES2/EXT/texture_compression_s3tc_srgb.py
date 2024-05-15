'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_EXT_texture_compression_s3tc_srgb'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_EXT_texture_compression_s3tc_srgb',error_checker=_errors._error_checker)
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT=_C('GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT',0x8C4D)
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT=_C('GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT',0x8C4E)
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT=_C('GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT',0x8C4F)
GL_COMPRESSED_SRGB_S3TC_DXT1_EXT=_C('GL_COMPRESSED_SRGB_S3TC_DXT1_EXT',0x8C4C)
