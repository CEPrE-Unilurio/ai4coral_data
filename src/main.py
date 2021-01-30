import fire
import superannotate as sa


def sa_upload_image_folder_files(conf_path:str="./conf.json", project_name:str, source:str):

    sa.init(conf_path)

    uploaded, skipped, duplicate = sa.upload_images_from_folder_to_project(
        project_name = project,
        folder_path = source,
        recursive_subfolders = True)

def sa_download_files(conf_path:object="./conf.json", project_name:str, destination:str):

    sa.init(conf_path)

    export = sa.prepare_export(project_name, include_fuse=True)

    sa.download_export(
        project = project_name,
        export = project_export,
        folder_path = destination)

def sa_convert_2_coco(conf_path:str="./conf.json", project_folder:str, destination:str,format='COCO', 
    project_type='Vector', 
    dataset_name='ai_coral',
    task='object_detection'):
    sa.export_annotation(
        project_folder,
        destination,
        format, 
        dataset_name,
        project_type,
        task
    )
    

def convert_coco_2_tfrecords(project_folder:str, destination:str):
    pass


if __name__ == '__main__':
    fire.Fire()
