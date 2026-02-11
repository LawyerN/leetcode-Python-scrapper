mask_sum_2bit = 0x5 => 0101
x = 0b1010

# Count number of bits in every consecutive 2 bits

x                           =>  1010
x & mask_sum_2bit           =>  0000
x >> 1                      =>  0101
x >> 1 & mask_sum_2bit      =>  0101
x = (x & mask_sum_2bit) + (x >> 1 & mask_sum_2bit ) =>  0101 # Result of computing the number of bits in every consecutive 2 bits

mask_sum_4bit = 0x3 => 0011

x                      => 0101
x & mask_sum_4bit      => 0001
x >> 2                 => 0001
x >> 2 & mask_sum_4bit => 0001
x = (x & mask_sum_4bit) + (x >> 2 & mask_sum_4bit) => 0010 # Result of computing the number of bits in every consecutive 4 bits