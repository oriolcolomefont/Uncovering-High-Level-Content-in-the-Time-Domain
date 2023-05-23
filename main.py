import train
import features
import eval


settings = [
    {
        "FILE_LIST_PATH": "./datasets/MSD/MSD_audio_limit=all_progress100_min_length_sr_16000.csv",
        "DATASET_NAME": "MSD partial",
        "BATCH_SIZE": 4,
        "CLIP_DURATION": 4.0,
        "SAMPLE_RATE": 16000,
        "MAX_EPOCHS": 1,
        "PATIENCE": 1,
        "EVAL_WINDOW": 0.5,
        "FEATURE": "embeddiogram",
    },
]

for setting in settings:
    try:
        train.FILE_LIST_PATH = setting["FILE_LIST_PATH"]
        train.DATASET_NAME = setting["DATASET_NAME"]
        train.BATCH_SIZE = setting["BATCH_SIZE"]
        train.CLIP_DURATION = setting["CLIP_DURATION"]
        train.SAMPLE_RATE = setting["SAMPLE_RATE"]
        train.MAX_EPOCHS = setting["MAX_EPOCHS"]
        train.PATIENCE = setting["PATIENCE"]

        fit, best_model_path = train.main()
        eval.FEATURE = setting["FEATURE"]
        eval.EVAL_WINDOW = setting["EVAL_WINDOW"]
        features.CKPT_PATH = best_model_path
        eval.main()
    except Exception as e:
        print(f"An error occurred while processing the settings {setting}. Error: {str(e)}. Continuing to the next iteration of the loop.")
