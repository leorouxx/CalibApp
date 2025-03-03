intrinsic_flags =  cv2.CALIB_FIX_K3# | cv2.CALIB_ZERO_TANGENT_DIST
ret, K_l, dist_l, rvecs, tvecs = cv2.calibrateCamera(objpoints, np.array(all_corners_l), (6000, 4000), None, None, flags=intrinsic_flags)
print(ret)
print(rvecs)
print(tvecs)
ret, K_r, dist_r, rvecs, tvecs = cv2.calibrateCamera(objpoints, np.array(all_corners_r), (6000, 4000), None, None, flags=intrinsic_flags)
print(ret)
print(K_l)
print(dist_l)
print(K_r)
print(dist_r)
raise SystemExit