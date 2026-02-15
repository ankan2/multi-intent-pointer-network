# #!/bin/bash
# . /home/nandy/miniconda3/etc/profile.d/conda.sh
# conda activate st
# nvidia-smi
# cd /home/nandy/PASTE
# pwd
# python3 PASTE_BERT.py --gpu_id 0 --src_folder 14res/ --trg_folder 14res/PASTE_BERT --bert_mode gen --gen_direct af --l2 y
# python3 PASTE_RoBERTa.py --gpu_id 0 --src_folder 14res/ --trg_folder 14res/PASTE_RoBERTa --bert_mode gen --gen_direct af --l2 y

# python3 PASTE_RoBERTa_coarse_intent.py --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_coarse_intent.txt

python3 PASTE_RoBERTa_fine_intent.py --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_fine_intent.txt

python3 PASTE_RoBERTa_coarse_intent.py --bs 32 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_bs_32 --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_bs_32.txt

python3 PASTE_RoBERTa_fine_intent.py --bs 32 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_bs_32 --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_fine_intent_bs_32.txt

python3 PASTE_RoBERTa_coarse_intent.py --bs 64 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_bs_64 --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_bs_64.txt

python3 PASTE_RoBERTa_fine_intent.py --bs 64 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_bs_64 --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_fine_intent_bs_64.txt

python3 PASTE_RoBERTa_coarse_intent.py --bs 128 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_bs_128 --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_bs_128.txt

python3 PASTE_RoBERTa_fine_intent.py --bs 128 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_bs_128 --bert_mode gen --gen_direct af --l2 y > hwu64_PASTE_RoBERTa_fine_intent_bs_128.txt

python3 PASTE_RoBERTa_coarse_intent.py --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_BW.txt

python3 PASTE_RoBERTa_fine_intent.py --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_fine_intent_BW.txt

python3 PASTE_RoBERTa_coarse_intent.py --bs 32 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_bs_32_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_bs_32_BW.txt

python3 PASTE_RoBERTa_fine_intent.py --bs 32 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_bs_32_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_fine_intent_bs_32_BW.txt

python3 PASTE_RoBERTa_coarse_intent.py --bs 64 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_bs_64_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_bs_64_BW.txt

python3 PASTE_RoBERTa_fine_intent.py --bs 64 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_bs_64_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_fine_intent_bs_64_BW.txt

python3 PASTE_RoBERTa_coarse_intent.py --bs 128 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_coarse_intent_bs_128_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_coarse_intent_bs_128_BW.txt

python3 PASTE_RoBERTa_fine_intent.py --bs 128 --gpu_id 0 --src_folder hwu64/ --trg_folder hwu64/PASTE_RoBERTa_fine_intent_bs_128_BW --bert_mode gen --gen_direct bw --l2 y > hwu64_PASTE_RoBERTa_fine_intent_bs_128_BW.txt
