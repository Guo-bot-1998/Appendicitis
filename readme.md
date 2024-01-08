2# 程式碼
皆上傳至[github](https://github.com/Guo-bot-1998/Appendicitis)

Colab:   
主要運行環境，<code>Appendicitis_colab_notebook.ipynb</code>處理所有事情(預處理->訓練->驗證)。  
Colab可直接pull/push單一筆記本。 

Vscode on Desktop:  
Colab不方便做時的選擇，只用Colab的話可無視其他程式碼。

# 資料存放
資料夾結構:

`test`

<pre>
AOCR2024
    ├── mask_bundle
    │   ├── Zx00AD16F8B97A53DE6E7CFE260BDF122F0E655659A3DF1628_label.nii
    │   └── Zx00AD16F8B97A53DE6E7CFE260BDF122F0E655659A3DF1628.nii
    ├── params
    │   └── Basic
    ├── sample_submission.csv
    ├── Test1_Image
    │   └── test_data
    ├── TrainValid_ground_truth.csv
    ├── TrainValid_Image
    │   ├── train_data
    │   └── valid_data
    ├── TrainValid_Mask
    │   └── train_mask
    └── TrainValid_split.csv
</pre>
存放於appendix2024ai@gmail.com之Google drive，colab可直接掛載   
<code>params</code>存放不同模型參數與hyper-parameter  
<code>mask_bundle</code>存放CT cut與對應mask  
其他依照kaggle格式  
