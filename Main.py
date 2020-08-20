__author__ = 'Brian M Anderson'
# Created on 8/20/2020

'''
First export the dose (preferably as a nifti file)
Also, export the exam as a nifti file
case.Examinations[exam.Name].ExportExaminationAsMetaImage(MetaFileName=r'H:\exam.mhd')
'''

import SimpleITK as sitk
import numpy as np
from Resample_Class.Resample_Class import Resample_Class_Object


resampler = Resample_Class_Object()
image_handle = sitk.ReadImage(r'H:\exam.mhd')
dose_handle = sitk.ReadImage(r'H:\dose.mhd')  # Doesn't currently exist
# dose_array = np.load(r'H:\dose_map.npy')
# dose_handle = sitk.GetImageFromArray(dose_array)

resampled_dose = resampler.resample_image(dose_handle, ref_handle=image_handle)
sitk.WriteImage(resampled_dose, r'H:\resampled_dose.nii.gz')
sitk.WriteImage(image_handle, r'H:\exam.nii.gz')
xxx = 1