# ML detection of QPSK signals transmitted over AWGN channel
import time
import numpy as np
frame_size = 1024; # frame size
SNR_dB = 9.5; # SNR per bit (dB)
SNR = 10**(0.1*SNR_dB) # SNR per bit in linear scale
noise_var_1D = 0.5/SNR # AWGN variance per dimension
sim_runs = 1e4 # simulation runs
C_BER = 0 # channel errors (TOTAL)
start_time = time.time()
#---------------------------------------
for i in range(int(sim_runs)):
 # source
 a=np.random.randint(2,size=2*frame_size)

 # QPSK mapping
 s = 1-2*a[0::2] + 1j*(1-2*a[1::2])

# AWGN
 awgn = np.random.normal(0,np.sqrt(noise_var_1D),frame_size)+1j*np.random.normal(0,np.sqrt(noise_var_1D),frame_size)

# channel output
 chan_op = s+awgn
 
# receiver
 # ML detection
 a_hat = np.zeros(2*frame_size)
 a_hat[::2] = chan_op.real<0
 a_hat[1::2] = chan_op.imag<0

 # calculating bit errors
 C_BER = C_BER + np.count_nonzero(a-a_hat)
  
 #-----------------------------------------------
elapsed_time = time.time() - start_time
# calculating Bit error rate
BER = C_BER/(2*frame_size*sim_runs)
print("elapsed time is: ",elapsed_time ,"seconds")
print("Bit error rate is: ",BER)


