import json

from streamlit import video

#It will load the data from inside the file and return the result
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) #This json load() automatically go inside the file and it will extract the data, load it and convert the string format data into in json then return it. 
    except FileNotFoundError:
        return [] #If File not exist then return empty list

#Whenever data has to be written inside the file we saved data here.
def save_data_helper():
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

# Created a function i.e; list_all_videos(all the videos will be returned from the server) that will return all the videos
def list_all_videos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}.")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():

    videos = load_data()

    # When I execute the program on the terminal constantly you have to ask the questions
    # Like if you ask me to press one then this function will run.............

    while True:
        print("\n Youtube Manager | choose an option...")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        Choice = input("Enter your choice: ")
        print(videos)

        match Choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)
        
            case _:
                print("Invalid Choice.")


#If functionname (name) is available anywhere inside the file, then run the main 
if __name__ == "__main__":
    main()