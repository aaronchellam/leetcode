from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_vol = max(max_vol, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol


    def compute_volume(self, height, left, right):
        return (right - left) * min(height[left], height[right])

if __name__ == '__main__':
    height = [488,8584,8144,7414,6649,3463,3453,8665,8006,1313,3815,7404,6969,7759,3643,8530,9792,1815,2480,6996,1151,2849,3432,1198,6125,1666,978,930,1678,3348,5223,2167,1932,3367,5933,4933,6830,9386,9951,1188,7051,118,8593,373,7877,2236,5255,7669,4051,7735,1018,1554,584,4450,9105,3061,2468,83,3992,498,9784,5567,2665,8068,8935,4951,3002,5765,4337,9305,3306,7741,9423,1899,8114,7301,487,3369,4970,890,7456,2340,8797,4392,6790,7902,3805,5610,7985,4149,6109,4121,9717,5126,2190,8652,77,1544,769,767,849,4075,8508,272,2326,2974,7573,9165,2695,8896,56,6503,1236,8853,7247,4379,6755,1052,9989,1092,5202,6098,5214,4919,7577,3756,9923,7654,5300,7044,8421,6149,1120,3281,6421,9798,2607,347,8964,5302,9243,5372,1805,479,4225,9052,1210,7332,6457,1200,8424,8011,3650,9990,9282,1227,3746,9205,5234,9046,6249,7,1547,3721,3289,4321,9872,5896,4668,8836,1199,3911,560,9356,742,4785,4761,1953,8469,1218,9505,3245,5581,9507,3236,4863,7087,3334,4068,2321,8733,6669,2328,280,391,1969,4601,6615,7866,9269,1803,5417,9532,2363,1125,6627,7148,5886,4932,1969,3456,4437,5214,9037,296,4802,252,7383,8137,4320,9704,6870,7342,8385,3502,4085,354,8104,700,4572,3725,2503,9989,9610,4866,7467,6237,8366,9705,1169,335,9514,1958,1901,4903,2254,6704,5156,9638,1193,9476,5694,8063,3170,4079,7917,7255,4434,2373,7955,9006,6099,458,5348,2061,1676,2815,8298,42,2520,5819,6729,2034,7777,8631,6938,31,5335,8446,6021,6528,7922,1716,943,1093,5795,8860,4700,6581,7586,2656,1940,3685,3114,3640,5746,4791,2807,396,1185,1679,6215,7915,3714,3992,6546,7004,375,8233,5450,6397,1113,9724,8113,8408,7169,260,3620,1870,3194,1206,4526,5134,4891,3992,5126,6989,5135,7933,3737,2673,9612,9952,588,9678,296,3486,3034,672,8071,4836,3421,9184,4561,1534,7592,8082,8146,7564,9952,1340,8771,830,2826,14,1175,7952,3356,2662,2237,7093,5335,1850,3398,2275,7880,3694,2113,915,718,184,5751,491,5720,6664,2025,3312,4747,6524,877,1051,7864,6000,8234,7043,6014,5761,1347,9370,8423,3585,6464,111,1787,6214,8738,9667,6260,852,6934,6979,1036,2686,3822,3109,5702,5848,6421,449,8724,3650,7853,6588,6002,2439,9983,2017,8200,1331,7739,2975,4916,555,9438,3055,6769,8177,9074,3030,5381,6009,6361,6417,5047,183,5878,749,2383,2300,7551,1107,2302,5404,4048,4657,7843,4031,6674,2395,1714,4413,5370,6630,4969,4809,6037,1738,9338,5112,1120,4719,1121,7481,7488,6168,4017,3367,6917,6400,2019,4468,7508,673,6224,7908,5330,419,8291,2004,2814,6,2770,8185,2988,4091,9346,9026,2181,8684,4138,3302,3403,1611,7135,891,7779,1152,4258,1048,7553,6277,1869,1413,6951,4445,5673,2281,4865,3964,638,7679,3970,3408,5864,6959,3851,5210,5985,6032,3894,6475,5686,3649,8086,2822,4541,5865,326,8799,3265,4231,5077,5134,5644,8380,9580,7669,661,797,1634,7651,8476,5604,7411,693,8915,1262,5903,4900,3647,6150,7727,9333,9799,5813,2155,692,8030,8834,9492,1296,3065,921,2782,5062,5653,8714,2731,2666,9511,4365,318,4340,6322,7729,5033,5237,8992,7288,6490,8991,9790,4217,8324,9590,31,6832,6634,4413,5666,6126,5709,8731,3399,4844,3793,9052,9910,6525,1719,9422,7242,8389,114,3564,6118,5147,8802,1462,2435,1644,453,2226,5861,8778,8168,2244,1962,4802,6658,7628,7281,8719,6359,7032,9915,153,6085,9826,3030,4156,5600,272,2545,5714,3837,5015,861,8991,6478,9648,6987,3283,8226,2848,8413,6394,1445,375,7549,4455,8003,1182,3174,715,8214,3090,7220,651,9268,250,1159,4868,6874,3704,582,7063,5072,7795,6054,1550,7443,3041,1185,5670,2242,9599,8416,39,6326,2317,4494,4330,3499,4020,1397,8066,3462,8617,5069,2730,5219,6229,7598,2093,6285,8180,9157,1357,5975,1563,9259,9771,957,445,5441,3199,6396,209,3238,2722,2527,4084,3404,2378,8104,4801,6796,1567,3418,1866,4297,4989,8095,8248,7083,732,6428,2592,2090,8756,4155,1349,8527,1464,1794,3968,4663,8190,529,4253,7265,9408,4689,669,8139,2794,5471,4935,713,5241,3153,1362,6583,7600,9610,3666,8333,6039,2610,423,1147,3117,1772,9674,4582,9919,9994,5597,4461,523,6203,1726,9932,892,8748,4423,38,571,9358,7103,2164,8864,8466,8747,6464,8076,8765,1149,467,1375,1572,1614,4493,9697,7640,5427,9616,7634,1024,429,4510,7227,8508,794,4472,7256,5217,4510,4179,927,1614,6343,9791,80,1443,2608,4508,208,3757,1328,1584,5330,9294,2429,1379,6935,7856,7347,921,8880,7776,5431,2460,2636,6225,6932,6244,7794,7794,423,8722,9408,3119,4865,5840,4562,7473,6701,4770,1231,4381,2706,2913,3675,5135,4292,6962,9343,1639,7884,8224,5767,9667,7036,8404,2245,3968,4648,39,1762,1424,5113,7523,4543,9979,9715,9105,7452,6416,227,8683,797,2934,1596,825,8069,2240,7787,3765,3879,2023,1989,9647,8043,5377,4403,288,5697,9051,327,3811,475,1793,1334,1370,1772,1050,475,9224,3818,703,4260,4616,9989,2208,5441,8058,4449,9580,8175,4680,7956,164,679,5999,1893,5082,6287,7590,486,2966,1402,7313,4759,2736,8684,6531,138,9159,2108,3957,6214,2720,4925,6203,4928,6718,614,5729,6298,8789,6762,4254,5306,7441,6605,3551,8876,2892,1142,9362,2211,2544,6675,6970,1632,5359,9854,8123,871,8314,2080,3437,1034,3357,5993,2314,75,2959,4396,2725,1748,1158,3332,3406,4951,9937,6958,3827,2830,4452,3189,5041,6996,6217,8363,4980,7928,4569,3103,8799,2883,1535,8589,269,4892,4582,8936,4967,7541,3332,7693,5641,842,1025,5400,5793,962,2358,9621,144,6810,9162,1537,158,5379,6253,1490,9660,822,4594,8459,58,6129,7048,327,7374,7982,5615,2341,5523,5299,6386,7517,6141,3763,2917,8287,1078,1627,4260,7574,4789,3422,9112,4947,5154,5365,2789,4814,2539,7383,9625,2597,9865,3026,9277,7239,1008,4892,5932,2884,192,8671,6753,2685,2434,9670,972,3512,7649,5232,1087,2438,5007,6551,3737,6513,8268,6526,1327,807,3910,7304,9757,127,330,9034,3718,7691,278,9650,6927,6822,8321,32,5860,7108,9702,6832,6972,7351,8417,8059,6141,3424,962,9878,9937,9230,6404,7616,6390,6666,1272,6147,3145,7955,1533,6863,1998,8163,2866,5277,4986,1187,5309,846,4647,1363,4030,1620,5066,2447,6031,1207,2223,6994,1085,8512,2576,3841,2480,8966,6860,3753,1465,5,1708,2998,6869,3706,7514,9735,8983,2500,7274,4292,9698,1922,2007,80,3542,7073,2528,9573,8280,1103,2919,5717,9616,5496,9558,2096,814,6418,2201,2280,6424,3909,1630,9645,3967,9144,9380,9302,7996,6654,9946,4046,4928,1953,4127,8470,9026,3007,4396,7306,462,7315,9375,6430,9163,8934,8527,9978,1704,7080,8610,4480,7342,240,4125,1309,5737,3505,612,85,6512,6910,4132,1440,8864,4611,6263,7890,3970,659,1549,4432,4326,7276,863,3490,6210,5742,9820,4267,2822,8430,5099,164,5022,9225,7826,759,9082,4790,7197,1946,1700,7681,3387,6916,2292,6002,1159,2614,6661,9060,7046,7339,6336,4261,829,8899,6355,7001,3166,5530,5431,4617,2046,454,3842,9872,7565,9277,1014,4762,7575,2715,2443,7314,5983,1087,3316,7142,3701,9977,6202,7100,3669,2539,1361,850,1438,4069,7852,956,9599,3283,5573,1645,3737,5768,1518,1303,1397,2532,2417,8972,1599,4861,6287,3935,5948,9603,1077,9650,5933,7280,6750,9602,6171,4463,452,3961,8532,8304,4917,4483,7940,6842,6129,8029,2610,3999,5684,4007,2883,8102,9332,4483,2963,5619,4770,5263,1574,5847,4913,7507,9479,8015,3461,5650,8831,266,9611,7363,4922,880,1847,2862,7723,4328,7244,6685,8327,2928,7045,1210,1030,6377,2045,345,8348,6815,5609,9922,2663,6874,3782,8494,4890,3595,4145,3721,3861,108,7436,8784,7341,5635,7998,1416,9963,5242,8101,4642,4523,5146,5853,1905,7875,4250,2251,2575,1066,4212,8850,81,1086,2632,8575,2328,2579,9072,6049,6441,5533,9838,1577,2874,1825,5927,4290,8141,1170,8743,2783,2045,242,4988,3950,4469,9239,6201,7045,305,6765,5895,6738,7852,4879,5313,180,7458,738,2582,251,6271,8772,8180,5497,597,4108,6139,5090,1630,4882,4226,3675,1476,9214,7625,5946,8453,179,2991,5110,6944,5238,1848,4796,6469,3514,1329,279,4252,263,6883,6875,9035,5063,2372,5984,9171,4863,1075,801,9745,5301,828,1222,867,8454,3520,5673,8633,2863,783,1929,8101,8984,6726,922,8850,4407,1201,9454,4670,8084,6329,3705,3148,5053,6041,8671,9916,7116,5825,6013,8769,6653,7235,9637,5107,7107,1662,92,9970,8797,2022,4423,7781,5100,5345,2983,9507,2899,2437,529,7335,8766,4234,483,171,275,5507,87,3744,1332,6101,8865,4337,9688,4854,9445,6796,6516,5889,6766,5314,4263,1190,9447,9363,2887,2431,5222,5786,4868,5751,3122,9987,6337,9957,158,2965,1816,6598,6709,3148,2699,1926,7486,8739,6781,3283,5535,9649,5524,8654,4963,9788,6196,4411,5503,9083,3194,726,1222,4414,2829,4344,753,9167,653,7264,2132,2470,3862,5193,1970,2913,7119,5808,1652,252,9091,3540,9902,968,2194,1217,7108,4742,1980,2611,3825,5174,9689,5047,5941,8871,5743,6694,8038,2749,3958,6522,5219,7820,8067,7189,7085,1538,9350,5090,1791,8441,8630,8045,5761,7176,9262,2869,1918,1243,5481,2095,2769,1522,3495,8710,393,9238,5405,4783,8339,9363,7657,3558,3536,5724,7100,6973,7263,6450,2063,5406,1243,7045,3451,7005,4221,9065,6226,2491,308,8059,4587,3078,9582,8082,8140,6327,3672,3545,1111,2012,9261,5120,1922,9149,845,9022,6122,4460,1824,4538,9866,3068,1583,9669,6425,5805,8734,9003,4648,5395,7063,9235,8473,2997,3669,2965,9324,3694,6511,6787,5706,2124,1908,3980,1273,9105,3003,3747,3565,1179,8285,9783,599,9869,9452,3376,2026,4538,2380,6674,9933,9443,2262,4758,8792,5931,7724,8116,9625,587,1256,1683,2711,9516,5664,3984,8621,5019,4083,2186,6198,2369,8321,3150,8590,4125,6526,616,8663,5258,3642,4949,4701,5904,6059,9845,8188,3783,7962,4165,722,5570,2201,3433,5086,7865,3769,3707,9236,7853,2245,1786,222,566,4936,8812,4691,7815,5780,9706,3073,5774,4655,4127,1679,7067,3972,6219,7202,8286,6736,7925,3856,8937,1358,8942,3154,1480,9001,2390,9333,1246,4177,5907,8164,5465,1071,2855,3280,6851,8914,2706,2625,9921,6833,656,6988,805,3227,4191,9092,9964,2116,9300,5253,9826,8243,8408,1306,3596,798,6991,4843,1327,9250,3007,3145,321,2215,2777,3524,7481,5483,2502,7402,2316,9510,4391,9474,2738,4934,4918,9054,7050,4218,4307,3228,8813,9067,887,2410,6218,7878,3605,7545,7129,2964,7042,3802,1531,9820,7327,9012,1655,9829,6415,324,9339,7158,9798,8429,2092,1068,3835,5494,5286,8143,5074,452,7210,5961,9214,3428,192,9171,7326,3673,2135,720,7475,19,540,1154,9031,2196,7335,1798,2520,6675,5308,8670,1456,7400,9738,5292,9246,1376,9787,4321,8180,3349,6634,7394,3130,6826,2917,456,499,1405,1176,4327,1424,8069,5481,6807,6617,2817,4958,9137,5844,266,4159,7300,4019,249,8944,3265,1625,8731,3938,6158,2081,573,9904,5211,7399,2822,2019,4251,4227,9547,8578,2003,7616,4059,8810,4233,3228,3768,9722,9072,387,233,2725,4406,482,1669,4023,8460,6753,4314,4618,8834,4887,4522,397,8638,3696,2416,2889,4275,8315,7819,6278,2284,1879,5089,2869,1459,5209,2592,532,1948,9177,3257,6354,9660,4926,6730,4472,1679,1044,9090,6865,5931,9964,3614,921,3661,2382,163,7936,698,7982,567,2982,6213,2008,5851,7673,3569,4795,8205,5518,3973,7814,8224,9985,9092,4954,4457,7124,5998,9899,3989,8281,6215,7604,5555,6228,6338,5718,517,7036,3700,1084,18,6266,3092,2222,3939,6661,7017,8496,2179,7342,6310,404,3679,5402,1710,4488,2526,4061,4387,2868,2342,6955,6824,4249,3183,3162,9967,3700,199,20,4784,6569,6286,4228,5143,225,890,8513,8721,9421,5855,5031,6177,5887,6785,4240,375,5664,8301,1115,8532,6995,8070,1708,1245,1253,4870,1212,1306,1421,1232,6090,4343,7518,6671,9486,4095,3913,7999,2816,9686,207,4199,5864,6094,7337,104,2821,3001,4757,3936,7885,1752,8358,9593,2997,5964,815,562,7270,2237,1794,9712,6580,5665,6383,2418,6112,296,418,5281,9983,625,5832,2199,3071,3169,8655,2244,2522,3412,2533,407,5164,891,0,4514,6855,7168,5076,477,9405,3222,190,2337,5239,2925,1107,1352,3222,1525,6633,9557,8502,2465,1756,7925,1987,6763,170,4509,175,2703,1269,1691,3594,7621,2557,6802,4789,7633,3631,546,7208,173,2883,8799,3099,343,151,2673,1868,3136,2230,6723,1954,338,4648,3941,7101,1170,4802,3628,3873,6071,1671,3820,3693,4229,6974,8482,8214,605,5381,5422,7131,4616,4222,230,4959,725,2903,3180,214,5133,9903,2168,1823,903,2461,8924,2074,7263,8904,2299,9687,575,2471,9732,4804,9445,4566,9371,6403,9947,1145,3534,4564,1719,116,9523,2445,3019,2703,2659,4504,8958,1179,2679,6214,3640,1603,4640,7255,507,6939,3294,7434,9411,3026,8591,5208,7593,7962,7963,7540,9107,1497,8456,827,7965,7980,9624,984,7035,2283,1840,5994,9814,4519,2208,3454,2474,6848,7061,9333,139,356,6768,5902,3382,1711,1111,7327,9673,9074,1220,8780,6924,9676,9607,4889,4008,9231,2226,1044,7866,418,3390,7680,1290,1950,7486,116,5150,4548,9450,1641,1256,2570,7544,990,4281,8655,8318,306,4081,9538,9086,7357,5566,5046,8599,9575,629,825,6971,4848,7595,361,2528,8885,8663,6367,9002,3813,7267,4804,5454,8523,3726,2998,9513,4359,8005,4183,4665,8439,3721,103,5796,5640,5149,4395,5215,5779,1572,2186,627,9168,8899,9507,4405,7562,5874,9759,1375,9493,915,3181,8016,993,2532,3882,5352,537,8065,6369,5328,8139,6473,1125,3779,1622,1872,5346,3753,3445,7532,4380,8965,2783,240,3370,345,2466,9482,8072,1960,397,1253,6328,1391,137,6562,3095,675,4628,9465,2355,9119,5938,9832,9250,3912,1705,4596,7666,1502,8480,8398,467,1263,8638,189,7960,7457,9671,6032,9417,6421,3637,2097,4164,3775,8660,7259,802,9640,3076,3157,8759,9014,2990,8009,9279,1047,8957,6945,2549,7437,5343,9368,5052,334,9557,3012,7791,5581,5396,3560,8354,9033,5657,2518,9160,669,6129,9962,309,9206,9472,9068,4572,8814,3429,3851,9861,8738,7148,8762,6175,2492,8130,7579,9178,7687,6943,3321,9620,2339,6881,7974,7725,8890,492,3237,9560,2974,9552,9869,8532,9024,5290,3104,4190,5071,3308,4051,3810,456,9165,6337,9300,7295,3917,4830,4982,860,8151,955,9552,5032,8929,3629,275,5774,6866,9835,8748,6418,9704,7280,1794,1346,6736,5984,6418,44,6387,228,6853,5552,6565,2505,9199,6834,7336,534,7695,5487,1489,3599,6872,418,3580,7147,6192,446,6982,4940,3217,3038,8572,1363,737,5309,3700,7155,1705,87,3735,4910,1992,300,7416,1191,7135,4752,1725,1182,6591,9566,1133,9815,9985,4713,6962,2529,1511,296,7470,1080,9687,2394,2444,424,4055,6144,3931,5761,2583,7666,671,927,4318,4439,8471,7805,5543,6548,5339,2135,6115,6472,8302,6100,7537,1617,8629,5401,1913,2451,6481,7952,1198,5277,4728,5253,7773,8659,1014,357,2677,8038,1284,6996,2477,6107,4801,8021,2656,141,6508,8771,2965,4810,1223,6855,6427,9852,2256,4693,8656,8737,8997,9854,367,3726,5107,8140,8737,2474,8497,1415,6864,6134,8411,5693,2241,9564,3714,1249,6057,6574,20,5375,7737,1243,2230,516,7448,4486,1561,2456,9575,559,2310,9942,4285,3769,4435,3022,2595,9284,789,9459,5418,9200,5153,4012,5117,5219,5261,1174,8146,1634,6549,5883,2877,5131,2751,6677,9617,4313,9133,5545,1224,7795,5487,5509,7917,9922,4883,512,9207,5673,6324,977,1225,7829,1341,6342,9400,2955,3869,7546,4589,6770,9781,3818,1902,8885,496,1519,3198,9629,7064,4422,7425,8904,6283,5342,5178,7518,2206,737,9543,4882,1715,769,2711,9408,3463,2112,2363,7332,6010,3304,455,2144,7123,2357,1029,7619,228,579,3600,3645,1353,7377,8901,3988,2719,4079,1506,1278,4817,1050,6160,2884,8171,8872,8644,1634,7336,7360,5319,9698,664,2126,8194,7787,4483,9223,1758,1063,6154,1711,1060,7507,9088,9961,7847,8160,393,5706,9438,1562,6756,5598,798,1279,822,9442,9265,4510,6802,936,4209,7467,3062,2403,1606,3897,7979,9717,1313,4133,1428,2373,7993,516,2335,2192,8676,9080,7898,4466,642,1006,65,1440,2285,7239,882,7903,1750,7685,8839,2311,1504,8254,1066,9462,2151,9045,9179,9816,9531,607,2190,3876,7476,877,6068,2504,9957,3967,6971,6951,4973,3388,8391,3611,627,9273,1514,8729,3310,353,1040,1166,4959,2107,629,3463,7504,6160,3279,7035,6768,1821,7263,596,2698,3332,3100,9007,3651,6423,5958,4976,9811,701,8587,439,6327,101,9168,5989,6807,6561,7156,1766,8668,4137,5229,2524,297,4861,5912,3417,6682,3175,365,5733,2859,3466,1092,2862,9889,3403,7839,6053,4104,6426,6492,431,2880,2012,6421,9687,4925,9929,7805,9945,418,3035,2470,7067,7896,8382,485,930,7909,7202,6663,7121,668,7756,9983,6910,1159,4174,2963,5263,601,5807,2047,9833,4171,4820,9520,9097,1101,7325,9042,1519,6712,7864,4938,960,2598,1775,1891,508,8978,4906,3981,9646,2662,3964,2908,173,4491,5871,1789,5092,8030,3836,4925,2202,5008,797,7651,6109,4474,3045,3980,7539,910,8918,8499,3508,7046,6742,368,6024,1649,701,5670,4311,1018,4931,837,5509,802,2626,601,5185,2814,1878,7387,7822,9027,1390,283,9853,4435,615,7392,5345,5885,5892,5206,2931,8986,1926,8955,635,2628,978,1299,3646,5909,2136,9155,3063,4762,6108,8248,3928,4338,1987,1750,9717,3377,8385,9570,7813,5352,6963,9510,1237,9207,1068,4169,8193,2995,9476,5181,1975,454,6480,1973,2715,8616,1128,5779,9730,3588,379,10,4278,2367,1760,3995,2096,6497,9917,6261,1849,6880,5772,3086,2439,3192,3607,6985,2539,9436,2166,4514,9890,8646,6487,8958,3614,3967,4737,9696,3907,1468,9706,8185,187,7818,8532,2284,667,8450,8545,2516,1682,669,1954,4122,3862,1914,7459,2753,1350,9625,7268,7592,4623,107,6550,4589,427,7639,4285,4334,5460,343,8872,5647,8161,3756,4283,5180,2206,9181,7696,241,9850,6002,715,64,7916,8174,2818,5618,4151,6438,3211,8774,2897,6113,3363,3324,3753,4000,4011,9213,4343,9235,1212,8856,2991,5496,4036,1550,4677,8084,1791,879,4086,2506,944,8355,7032,114,3973,1183,2904,7184,9957,5801,9650,9672,5478,3403,3672,9489,8968,4367,5076,6532,3223,8067,2028,3611,5969,6705,1695,7760,3937,2133,6618,1233,488,3650,1347,4462,1185,603,7998,7494,6404,7648,7166,1882,7403,838,7723,6371,1557,2799,9256,4780,867,1284,4743,3188,4342,6438,949,8279,8572,3919,9512,9060,3922,7211,9874,5107,4166,7873,2602,570,5521,6120,8805,2925,3311,6528,5648,4868,9328,4904,9649,6547,2541,4392,9735,3235,7183,7036,1514,2107,7308,7378,7519,1230,941,7394,2689,5107,1619,1643,2029,7140,7764,834,6417,1075,3715,8418,5943,9395,9674,1944,2294,2215,2689,8381,5450,9872,5418,3316,8331,2726,7046,5850,308,7987,9596,2997,9446,1215,4641,7828,4708,8757,5014,7477,9832,8729,2247,5775,4476,1922,4072,6770,489,6761,5152,5940,2985,6922,5608,1316,9648,2655,3518,6308,6994,9467,5657,2793,7034,6650,621,1742,5407,5635,5572,5239,4365,7819,7367,8841,9741,1439,1964,231,8200,7116,2523,7537,4038,8131,5205,38,7138,8723,2698,4133,4542,8355,6926,1577,5006,7547,9671,413,9534,5243,2005,251,9415,9372,5445,9156,7163,7409,5739,1715,4525,4614,9252,4915,9098,4457,1305,6236,9532,4003,369,4075,2358,3647,5652,3716,7546,5323,482,7081,6919,2487,7332,6334,1859,2777,1842,5374,6538,7582,7089,7415,8548,6341,2330,7646,7150,9987,3883,3034,3990,604,7109,2701,604,9113,6417,8150,789,6899,1583,7708,5738,5268,4042,3949,4397,5884,9323,936,9818,6412,8351,8367,9105,7034,2365,6255,7021,2600,5642,7364,9557,2751,6417,161,8217,2834,4663,9006,6086,6247,6714,1824,7867,7108,2126,2264,9344,1449,3200,9163,7862,7904,3882,3319,1290,2599,5927,4663,5200,1569,8379,4757,672,4796,1270,8889,3983,5933,7895,69,8532,961,8245,6399,4421,371,5016,3766,8173,4568,9281,6035,8824,9515,5706,114,2114,1633,4778,3666,3202,9509,8423,3875,4306,9693,9116,8289,1979,3364,4710,511,4325,9307,3263,5099,6031,8279,8865,4204,2847,4498,6591,1672,4013,2297,8138,2479,3931,9268,6146,3485,8778,4569,3712,3084,615,2829,7725,2594,6193,2435,9457,6870,1742,2720,1969,4125,7351,7186,8329,6551,8036,4920,4575,2049,3570,2713,881,3853,8334,7027,3690,7112,7948,7403,6548,4915,232,4273,3861,2777,3060,3319,5999,4802,2391,7969,8928,9743,1507,3609,2646,9544,4882,7221,7945,8452,6286,8826,8657,4620,2205,2347,1732,6506,9750,4632,1421,6334,8905,5283,9111,1965,4954,5111,3120,7345,9432,8400,3440,7291,8361,6086,6835,3243,9659,4781,8047,5946,9959,6704,566,8517,9052,8651,5023,8802,3283,2796,5137,8541,4431,600,6858,9385,2063,6330,3083,7847,1082,6523,5139,9444,8962,8326,2687,8621,9459,7087,4567,9419,3791,1486,4288,2843,137,9311,7998,9772,2107,3135,8313,6539,87,5172,2276,8503,7854,5359,6350,8937,8235,7841,4733,7197,6168,3772,2170,5627,859,3090,1398,4651,4576,5686,7494,4713,1349,1844,4485,3457,1331,9151,6348,1419,675,4976,6274,8529,6688,8976,3818,4923,6818,8551,8472,2986,2324,642,4965,3183,3732,6364,7834,8308,8402,1681,9373,9752,3525,211,9561,1209,9362,2261,2628,37,7237,5254,8566,3925,4230,2385,5200,1048,936,3672,386,3260,667,1704,2796,751,8068,6982,5412,2822,5015,4785,2574,4893,4996,2135,6102,4358,4396,5082,747,7986,336,9314,1911,4566,8051,7112,1967,5339,7136,2353,4952,7803,4057,7748,8555,8477,4730,3967,1300,6098,5104,3874,991,6453,2362,7093,7163,6758,2175,7911,4744,2511,3577,3008,3429,1628,6472,5396,3319,3608,7750,8271,7764,8159,2371,6319,2989,3454,6638,4289,9552,8094,4515,543,4547,6877,7636,8063,9988,6163,5974,1084,8674,5903,4092,2103,3883,6916,3852,7202,525,1602,1826,8289,6113,4197,960,9102,7651,3950,9743,7203,8396,611,4098,9296,7488,1734,7359,3828,4249,9685,4913,9275,5588,5357,7731,9471,2274,1583,3025,9151,9537,4851,3792,5650,9049,1104,1105,6700,1406,848,256,9802,1459,4354,9098,5300,2441,6457,5480,6690,6142,6745,5966,1730,2103,3697,7553,729,5280,579,6232,4817,5430,6376,6819,4479,7480,7924,7532,8886,5125,7788,8688,2936,8494,4139,4588,935,596,69,7626,3091,6814,9944,1173,5269,9993,8727,2350,1625,5658,4934,6442,1088,1310,9613,1920,5142,3890,5804,4028,9015,9944,9069,8303,8438,3208,2892,5726,156,9313,3352,3247,2479,9648,4421,7749,9641,9500,6451,1266,5158,1386,4060,2598,9048,3673,4518,4191,3915,6674,4571,2930,6618,3640,7586,1409,3200,6830,7135,3357,6143,6839,6604,8622,6487,7377,2723,2480,6877,9175,98,8387,6913,4158,986,2313,4183,1856,6504,8099,8531,1076,7381,1501,1068,4967,2910,4269,1797,45,7626,4292,3236,582,2915,9723,4312,1990,8555,7541,7517,8653,5929,782,9163,6915,3096,3347,5123,9600,7798,3654,7028,1531,1508,8097,6499,4418,8718,4648,816,2696,5293,4052,3278,4560,128,3942,6550,8683,1484,4068,3689,7413,4850,2852,680,4298,2551,5803,3899,349,5810,7279,1881,7318,5376,4732,8088,446,5732,5256,3142,1025,9309,2773,5585,5789,6715,8488,824,8199,8908,4513,5612,110,7366,2644,4409,9917,8448,4660,6619,610,1939,4852,7928,3668,5936,2368,4114,8020,7625,7257,9046,3286,30,983,9075,6745,5823,6251,1297,4731,765,6909,4842,4483,5906,9251,752,4354,3911,7371,4964,2202,8575,9244,5870,863,1612,9985,8884,5589,7242,4282,8875,3624,1617,4302,369,7441,554,8018,2172,7671,1280,3366,2154,7186,8969,2906,7892,9232,278,2856,1435,5205,8452,7305,6069,6416,7290,4953,2006,884,5587,7233,4508,7204,1536,1230,4645,8442,9248,3170,6113,528,6536,8267,7714,1858,1173,1958,1090,7803,4814,2525,9361,9618,9831,5430,6035,3473,6735,4393,4358,2322,1626,5218,9526,3162,2800,524,7956,8401,3694,4069,5281,6582,8688,2996,4792,6214,1306,5883,369,6121,4760,9730,2091,4591,1512,8126,4417,8247,8871,5127,6921,498,345,2800,3660,9498,3324,7969,7899,3370,2038,3180,6304,727,2528,1097,3293,3835,3332,3662,6308,8092,3393,8399,9036,4905,2878,3453,9505,1749,8580,2778,8599,5277,5578,2260,4775,8902,229,9026,8624,8619,8559,4929,5698,1087,2378,8991,1274,5710,2654,7582,3802,2399,2334,2838,3656,1564,6291,3161,9665,1223,5940,8265,6501,7870,6877,7628,3125,3458,3007,1749,8429,1566,3030,4128,9005,5408,9471,280,1118,8477,4214,1273,876,2900,4111,4533,816,6755,4046,482,7978,6338,5099,831,4209,8328,4812,7334,1786,7819,5435,215,5737,8466,695,4742,226,6519,5022,1345,4996,5589,8970,2225,8489,3081,6758,5658,6188,7156,6140,4167,3495,7591,1350,4056,5919,6162,1390,4057,333,6825,624,6070,1643,7672,813,1870,4191,2187,9567,9187,7776,8537,7764,2618,7970,874,8276,4159,8031,768,4678,7878,4711,6028,1934,630,8543,9676,4687,5228,2853,5311,1299,4497,2983,8464,6367,3526,7003,5934,9066,1132,823,6830,3750,8793,7705,8378,2952,2088,5498,3982,9966,209,6363,8252,839,4906,7928,1878,6486,781,3541,7785,5278,2877,2601,7997,6403,9605,283,5469,737,1106,8652,839,9900,6357,5569,9204,8445,1067,9539,4763,7628,5902,3015,4819,7160,943,6697,3646,8076,6590,7784,9707,9467,385,7704,2223,6342,7988,4044,7079,5446,9048,4270,1698,5405,9839,7255,202,7258,6794,1317,4886,2696,4332,9705,9856,1627,2754,3502,6056,9345,7638,5763,5164,8024,3467,3739,4366,7807,4136,7798,9606,3184,2068,1304,8590,8260,4911,5144,5518,1705,2814,405,753,7146,110,609,5126,2865,464,7534,8562,8102,3297,3726,2478,3116,3818,3197,7276,7954,995,6882,1138,9415,4538,6080,7675,9450,1225,3194,7507,391,3599,8261,7537,61,5222,9015,9278,5686,6549,7840,141,6198,1567,8971,9315,5385,2168,2943,9691,9515,9825,829,8931,715,6910,6606,6517,4487,6152,4025,4878,6103,2286,8767,6165,7508,4135,5443,9547,7036,3284,6040,3235,1203,5011,2550,2940,7180,5493,2631,6695,1670,9812,1978,8737,6722,8585,5255,1209,1089,9280,2439,7193,7918,1207,9710,1778,5342,1505,7677,2378,4789,3717,1965,2344,8729,867,1636,2261,2712,619,5308,4382,432,7287,9472,3506,2224,4727,1068,3313,359,3507,6858,4629,1066,6568,6407,6408,8074,437,5139,9215,4154,7104,7912,9235,4324,5900,7848,7036,6520,3157,7771,3304,444,7243,6810,2668,1970,7878,2333,8681,7738,9192,3310,8804,2112,6069,1565,6538,6506,6704,5754,7013,160,18,6248,836,5918,449,7873,2438,3606,5644,2094,402,2887,8905,9422,1209,3135,1755,9890,873,7299,3200,9678,9412,9269,1243,2302,2128,4299,8056,9141,811,4426,1741,1648,345,2190,9521,9135,2148,1517,1230,2550,756,6487,1972,1965,9622,80,8207,496,7379,7759,6526,3143,3380,4121,5446,5508,8420,9854,1001,5583,633,2743,7231,978,4933,3104,6465,3434,4621,4047,5984,5377,534,4309,3694,157,4389,8253,7005,8120,2364,9883,7616,5745,4004,9414,7605,2424,5620,8607,8007,6253,7702,1591,3583,8987,4695,6401,2421,5669,448,8406,7398,983,9067,7445,7492,9808,5698,849,7928,8063,732,1896,160,4736,7662,4117,3512,3283,2724,7871,5888,6778,9462,5824,5766,510,2225,8187,6179,2673,2945,9929,8,2012,7374,7500,1820,3073,4701,6101,7488,5433,4349,4000,169,2012,8117,33,1647,7194,7905,7535,3972,7367,9711,9738,4229,1936,4278,408,962,7223,338,970,9236,4064,4823,7408,7137,9524,9861,977,4958,4211,1329,1479,2575,5799,1513,4222,2993,5770,8109,3317,3137,7821,9408]
    sol = Solution().maxArea(height)
    print(sol)