"""
*********** Performance Prediction Toolkit PPT *********

File: GPU_config.py
Description: Target GPU configurations
Author: Yehia Arafa 
"""

import sys 
from arch_latencies_config import *



def get_gpu_config(gpu):
    new_gpu = gpu()
    config = new_gpu.populate_config()
    return config


class K40m():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "K40m"
        config["gpu_arch"] = "Kepler" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))
       
        config["num_SM"]                     = 15           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 192          # Number of Single Precision cores per multiprocessor  
        config["num_SF_per_SM"]              = 32           # Number of Special Function units per multiprocessor 
        config["num_DP_per_SM"]              = 64           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 32           # Number of Load & Store units per multiprocessor
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 745*10**6    # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 
        
        config["l1_cache_size"]              = 16*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 1.5*10**6    # L2 cache size in Bytes
        config["global_mem_size"]            = 12*10**6	    # Global memory size in Byte
        config["shared_mem_size"]            = 48*10**3 	# Shared memory size in Bytes per multiprocessor 

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]
        
        config["warp_size"]                  = 32		    # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64		    # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32		    # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024		    # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048		    # Max number of threads queued or active on a single SM
        
        config["global_mem_return_queue"]    = 128		    # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1            # Number of memory ports

        return config


class Titanx():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "TitianX"
        config["gpu_arch"] = "Maxwell" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))
       
        config["num_SM"]                     = 24           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 128          # Number of Single Precision cores per multiprocessor  
        config["num_SF_per_SM"]              = 32           # Number of Special Function usints per multiprocessor 
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 32           # Number of Load & Store units per multiprocessor
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1000*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 
        
        config["l1_cache_size"]              = 48*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 3*10**6	    # L2 cache size in Bytes
        config["global_mem_size"]            = 12*10**6	    # Global memory size in Byte
        config["shared_mem_size"]            = 64*10**3		# Shared memory size in Bytes per multiprocessor 

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]
        
        config["warp_size"]                  = 32		    # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64		    # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32		    # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024		    # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048		    # Max number of threads queued or active on a single SM
        
        config["global_mem_return_queue"]    = 128		    # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports "]          = 1

        return config


class P100():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "P100"
        config["gpu_arch"] = "Pascal" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))
       
        config["num_SM"]                     = 56           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor  
        config["num_SF_per_SM"]              = 16           # Number of Special Function usints per multiprocessor 
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1190*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 
        
        config["l1_cache_size"]              = 24*10**3     # L1 cache size in Bytes  
        config["l2_cache_size"]              = 4*10**6	    # L2 cache size in Bytes
        config["global_mem_size"]            = 16*10**6	    # Global memory size in Byte
        config["shared_mem_size"]            = 64*10**3		# Shared memory size in Bytes per multiprocessor 

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]
        
        config["warp_size"]                  = 32		    # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64		    # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32		    # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024		    # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048		    # Max number of threads queued or active on a single SM
        
        config["global_mem_return_queue"]    = 128		    # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config


class V100():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "V100"
        config["gpu_arch"] = "Volta" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))
       
        config["num_SM"]                     = 60           # Number of Streaming Multiprocessors 
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per multiprocessor  
        config["num_SF_per_SM"]              = 4            # Number of Special Function usints per multiprocessor 
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per multiprocessor 
        config["num_load_store_units"]       = 16           # Number of Load & Store units per multiprocessor
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp 
        config["clockspeed"]                 = 1246*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available 
        
        config["l1_cache_size"]              = 128*10**3    # L1 cache size in Bytes  
        config["l2_cache_size"]              = 6*10**6	    # L2 cache size in Bytes
        config["global_mem_size"]            = 12288*10**6	# Global memory size in Byte
        config["shared_mem_size"]            = 96*10**3		# Shared memory size in Bytes per multiprocessor 

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]
        
        config["warp_size"]                  = 32		    # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64		    # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32		    # Max number of blocks queued on a single SM 
        config["max_num_threads_per_block"]  = 1024		    # Max number of (software) threads in a block 
        config["max_num_threads_per_SM"]     = 2048		    # Max number of threads queued or active on a single SM
        
        config["global_mem_return_queue"]    = 128		    # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config

# NVIDIA Tesla V100-SXM2-16GB on LLNL Sierra systems.
# Specs from:
# - https://hpc.llnl.gov/training/tutorials/using-lcs-sierra-system#Volta,
# - https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018
# - https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf
# - https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
class V100_SXM2_16GB():

    def populate_config(self):
        config = {}
        config["gpu_name"] = "V100_SXM2_16GB"
        config["gpu_arch"] = "Volta" #This name must be one of the classes defined in 'arch_latencies_config'

        mem_latencies = get_mem_latencies(getattr(sys.modules[__name__], config["gpu_arch"]))

        config["num_SM"]                     = 80           # Number of Streaming Multiprocessors
        config["num_SP_per_SM"]              = 64           # Number of Single Precision cores per SM
        config["num_SF_per_SM"]              = 4            # Number of Special Function units per SM
        config["num_DP_per_SM"]              = 32           # Number of Double Precision cores per SM
        config["num_load_store_units"]       = 32           # Number of Load & Store units per SM
        config["num_warp_schedulers"]        = 4            # Number of warp schedulers available (Max number of warps that can be executed concurrently)
        config["num_inst_per_warp"]          = 2            # Number of instructions that can be issued simultaneously to a given warp
        config["clockspeed"]                 = 1312*10**6   # GPU clock speed in Hertz

        config["num_registers"]              = 65536        # Number of registers available

        config["l1_cache_size"]              = 128*10**3    # L1 cache size in Bytes
        config["l2_cache_size"]              = 6144*10**3   # L2 cache size in Bytes
        config["global_mem_size"]            = 16*10**9     # Global memory size in Bytes
        config["shared_mem_size"]            = 96*10**3     # Shared memory size in Bytes per SM

        config["l1_mem_latency"]             = mem_latencies["l1_cache_access"]
        config["l2_mem_latency"]             = mem_latencies["l2_cache_access"]
        config["l2_to_global_mem_latency"]   = mem_latencies["global_mem_latency"] - mem_latencies["l2_cache_access"]
        config["local_mem_latency"]          = mem_latencies["local_mem_latency"]
        config["const_mem_latency"]          = mem_latencies["constant_mem_latency"]
        config["tex_mem_latency"]            = mem_latencies["texture_mem_latency"]
        config["tex_cache_latency"]          = mem_latencies["texture_cache_latency"]
        config["shared_mem_latency"]         = mem_latencies["shared_mem_latency"]

        config["warp_size"]                  = 32           # Number of threads in a warp
        config["max_num_warps_per_SM"]       = 64           # Max number of warps resident on a single SM
        config["max_num_block_per_SM"]       = 32           # Max number of blocks queued on a single SM
        config["max_num_threads_per_block"]  = 1024         # Max number of (software) threads in a block
        config["max_num_threads_per_SM"]     = 2048         # Max number of threads queued or active on a single SM

        config["global_mem_return_queue"]    = 128          # Number of memory concurrent transfer from the memory queue
        config["num_memory_ports"]           = 1

        return config
