import lc4
key = "pq_xc589r3nb#mgjtkh7w2dlfvy4eaoi6uzs"
encrypted = "wpwt#5ng4_qbitp#8mq59r_g866c4t59c6vy6tisj4af6bprfnbd_wrq2wjmr4ld_s26a7i#biiyqjolq8lus_wfusfkj8xv2qrrv3etab_marovc#uuoueyl"

decrypted = lc4.decrypt(key, encrypted)
print(decrypted)
