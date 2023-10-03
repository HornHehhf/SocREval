import json
import pandas as pd


def process_roscoe_explain_then_predict(dataset="gsm8k"):
    dir_path = "/path/to/working/dir/"
    raw_path = dir_path + "roscoe/raw/{}.txt".format(dataset)
    annotated_path = dir_path + "roscoe/annotated/{}.csv".format(dataset)
    data_path = dir_path + 'ROSCOE/{}_roscoe_annotations.json'.format(dataset)
    with open(raw_path) as rf:
        raw_lines = rf.readlines()
    annotated_data = pd.read_csv(annotated_path)
    data = []
    for index in range(len(annotated_data)):
        metadata_example_idx = annotated_data.loc[index, 'metadata_example_idx']
        metadata_generation = annotated_data.loc[index, 'metadata_generation']
        human_judged_overall_quality = annotated_data.loc[index, '0_full_newOverall_result']
        raw_example = json.loads(raw_lines[metadata_example_idx].strip())
        annotated_example = raw_example
        annotated_example['metadata_example_idx'] = str(metadata_example_idx)
        annotated_example['metadata_generation'] = metadata_generation
        annotated_example['0_full_newOverall_result'] = str(human_judged_overall_quality)
        data.append(annotated_example)
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)


def process_roscoe_predict_then_explain(dataset):
    dir_path = "/path/to/working/dir/"
    restore_annotated_path = dir_path + "roscoe/restore_annotated/{}.json".format(dataset)
    annotated_path = dir_path + "roscoe/annotated/{}.csv".format(dataset)
    data_path = dir_path + 'ROSCOE/{}_roscoe_annotations.json'.format(dataset)
    examples = []
    with open(restore_annotated_path) as raf:
        lines = raf.readlines()
    for line in lines:
        examples.append(json.loads(line.strip()))
    annotated_data = pd.read_csv(annotated_path)
    data = []
    for index in range(len(annotated_data)):
        metadata_example_idx = annotated_data.loc[index, 'metadata_example_idx']
        metadata_generation = annotated_data.loc[index, 'metadata_generation']
        human_judged_overall_quality = annotated_data.loc[index, '0_full_newOverall_result']
        raw_example = examples[metadata_example_idx]
        annotated_example = raw_example
        annotated_example['metadata_example_idx'] = str(metadata_example_idx)
        annotated_example['metadata_generation'] = metadata_generation
        annotated_example['0_full_newOverall_result'] = str(human_judged_overall_quality)
        data.append(annotated_example)
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    process_roscoe_explain_then_predict(dataset="gsm8k")
    process_roscoe_predict_then_explain(dataset="drop")
    process_roscoe_predict_then_explain(dataset="esnli")
    process_roscoe_predict_then_explain(dataset="cosmos")

