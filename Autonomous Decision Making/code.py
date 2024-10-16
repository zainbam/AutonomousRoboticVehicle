# -*- coding: utf-8 -*-
"""AutonomousNavigation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uEEnHocFDLv0A203A8w1HyxZK9djmL6G
"""

from google.colab import files

uploaded = files.upload()

import json

# Specify the path to the uploaded file
uploaded_file_path = '/content/directions_data.json'

# Load the data from the file
with open(uploaded_file_path, 'r') as file:
    loaded_data = json.load(file)

distance = loaded_data["routes"][0]["legs"][0]["distance"]["text"]
print(f"Total Distance: {distance}")



from math import radians, sin, cos, sqrt, atan2

data = loaded_data

def haversine_distance(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate distance in kilometers
    distance_km = R * c

    # Convert distance to meters
    distance_meters = distance_km * 1000

    return distance_meters

def simulate_driving(data):
    steps = data["routes"][0]["legs"][0]["steps"]

    # Initialize direction as "straight"
    direction = "straight"

    for i, step in enumerate(steps, start=1):
        print(f"Drive {direction} until the next instruction.")
        print(step["html_instructions"])
        print(direction)
        # Extract start and end locations for each step
        start_location = step["start_location"]
        end_location = step["end_location"]

        print(f"Start Location: {start_location['lat']}, {start_location['lng']}")
        print(f"End Location: {end_location['lat']}, {end_location['lng']}")
        print("---------------------")

        # Check if there is a turn instruction
        if "maneuver" in step:
            # Keep asking for coordinates until the user is within 5 meters of the turn
            while True:
                # Ask user to enter coordinates
                user_coordinates = tuple(map(float, input("Enter coordinates (lat, lon) in decimal degrees: ").split(',')))

                # Check distance between user coordinates and turn start location
                distance = haversine_distance(user_coordinates, (start_location['lat'], start_location['lng']))
                print(f"Distance to Turn {i-1} start location: {distance} meters")

                # Check if user is near the turn
                if distance <= 5:
                    print(f"You have completed Turn {i-1}!")
                    # Update direction based on the turn instruction
                    direction = step["html_instructions"].split('<b>')[1].split('</b>')[0].lower()
                    print(direction)
                    break  # Exit the loop if the user is within 5 meters
                else:
                    print(f"Keep going. This is not the turn. Continue driving {direction}.")

simulate_driving(loaded_data)

class RoboticCarDecisionMaker:
    def __init__(self):
        # Initialize some variables for the current state
        self.closest_object_distance = float('inf')  # Start with a large distance
        self.closest_object_class = None
        self.closest_object_bbox = None
        self.current_direction = "straight"  # Start with a default direction

    def update_state(self, distances, obj_classes, bboxes):
        # Update the state with the latest object detection information
        objects = zip(distances, obj_classes, bboxes)
        sorted_objects = sorted(objects, key=lambda x: x[0])  # Sort based on distance
        self.closest_object_distance, self.closest_object_class, self.closest_object_bbox = sorted_objects[0]

    def make_decision(self):
        # Decision-making logic based on the current state

        # Check if there is an obstacle within a safe distance
        if self.closest_object_distance < 2.0:  # Adjust the threshold as needed
            if self.closest_object_class == "car":
                # Check if the closest object is a moving car
                if self.is_moving_car():
                    self.avoid_collision()
                else:
                    self.stop_and_wait()
            elif self.closest_object_class == "person":
                self.stop_and_yield_to_pedestrian()

        # Check for changes in direction
        if self.is_direction_change_needed():
            self.adjust_direction()

    def is_moving_car(self):
        # Logic to determine if the closest object is a moving car
        # You may use additional information or machine learning models for this
        return True  # Placeholder, replace with actual logic

    def avoid_collision(self):
        # Logic to avoid collision with a moving car
        # Implement your own collision avoidance strategy
        print("Collision detected! Taking evasive action.")

    def stop_and_wait(self):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        print("Stopping and waiting for the obstacle.")

    def stop_and_yield_to_pedestrian(self):
        # Logic to stop and yield to pedestrians
        # Implement your own strategy for yielding to pedestrians
        print("Stopping and yielding to pedestrians.")

    def is_direction_change_needed(self):
        # Placeholder logic, replace with your own
        # Check if the direction needs to be changed based on some criteria
        return True

    def adjust_direction(self):
        # Placeholder logic, replace with your own
        # Implement logic to adjust the direction of the robotic car
        print("Adjusting direction.")

# Example usage:
decision_maker = RoboticCarDecisionMaker()

# Update state with object detection information
distances = [1.5, 1.8, 3.0]  # Replace with actual distances
obj_classes = ["car", "person", "car"]  # Replace with actual classes
bboxes = [((0, 0), (10, 10)), ((5, 5), (15, 15)), ((2, 2), (12, 12))]  # Replace with actual bounding boxes

decision_maker.update_state(distances, obj_classes, bboxes)

# Make decision based on the updated state
decision_maker.make_decision()

class RoboticCarDecisionMaker:
    def __init__(self):
        # Initialize some variables for the current state
        self.closest_object_distance = float('inf')  # Start with a large distance
        self.closest_object_class = None
        self.closest_object_bbox = None
        self.current_direction = "straight"  # Start with a default direction

    def update_state(self, distances, obj_classes, bboxes):
        # Update the state with the latest object detection information
        objects = zip(distances, obj_classes, bboxes)
        sorted_objects = sorted(objects, key=lambda x: x[0])  # Sort based on distance
        self.closest_object_distance, self.closest_object_class, self.closest_object_bbox = sorted_objects[0]

    def make_decisions(self):
        # Decision-making logic based on the current state for all objects

        for distance, obj_class, bbox in zip(distances, obj_classes, bboxes):
            # Update the state for the current object
            self.closest_object_distance = distance
            self.closest_object_class = obj_class
            self.closest_object_bbox = bbox

            # Print parameters for the current object
            print(f"Object: {obj_class}")
            print(f"Distance: {distance}")
            print(f"BBox: {bbox}")
            print("Making decision...")

            # Check if there is an obstacle within a safe distance
            if distance < 2.0:  # Adjust the threshold as needed
                if obj_class == "car":
                    # Check if the object is a moving car
                    if self.is_moving_car():
                        self.avoid_collision()
                    else:
                        self.stop_and_wait()
                elif obj_class == "person":
                    self.stop_and_yield_to_pedestrian()

            # Check for changes in direction
            if self.is_direction_change_needed():
                self.adjust_direction()

    def is_moving_car(self):
        # Logic to determine if the closest object is a moving car
        # You may use additional information or machine learning models for this
        return True  # Placeholder, replace with actual logic

    def avoid_collision(self):
        # Logic to avoid collision with a moving car
        # Implement your own collision avoidance strategy
        print("Collision detected! Taking evasive action.")

    def stop_and_wait(self):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        print("Stopping and waiting for the obstacle.")

    def stop_and_yield_to_pedestrian(self):
        # Logic to stop and yield to pedestrians
        # Implement your own strategy for yielding to pedestrians
        print("Stopping and yielding to pedestrians.")

    def is_direction_change_needed(self):
        # Placeholder logic, replace with your own
        # Check if the direction needs to be changed based on some criteria
        return True

    def adjust_direction(self):
        # Placeholder logic, replace with your own
        # Implement logic to adjust the direction of the robotic car
        print("Adjusting direction.")

# Example usage:
decision_maker = RoboticCarDecisionMaker()

# Example arrays for distances, obj_classes, and bboxes
distances = [1.5, 2.0, 3.0]  # Replace with actual distances
obj_classes = ["car", "person", "car"]  # Replace with actual classes
bboxes = [((0, 0), (10, 10)), ((5, 5), (15, 15)), ((2, 2), (12, 12))]  # Replace with actual bounding boxes

# Make decisions based on the updated state for all objects
decision_maker.make_decisions()

class RoboticCarDecisionMaker:
    def __init__(self):
        # Initialize some variables for the current state
        self.closest_object_distance = float('inf')  # Start with a large distance
        self.closest_object_class = None
        self.closest_object_bbox = None
        self.current_direction = "straight"  # Start with a default direction
        self.previous_closest_object_distance = 1.498
        self.previous_closest_object_class = 'car'
        self.speed_distance_threshold = 0.05  # 5% threshold for speed difference

    def update_state(self, distances, obj_classes, bboxes):
        # Update the state with the latest object detection information
        objects = zip(distances, obj_classes, bboxes)
        sorted_objects = sorted(objects, key=lambda x: x[0])  # Sort based on distance
        self.closest_object_distance, self.closest_object_class, self.closest_object_bbox = sorted_objects[0]

    def track_closest_object_state(self):
        # Track the state of the closest object over consecutive frames
        if self.previous_closest_object_distance is not None and self.previous_closest_object_class == self.closest_object_class:
            # Calculate the percentage difference in distances
            percentage_difference = abs(
                (self.closest_object_distance - self.previous_closest_object_distance) / self.previous_closest_object_distance
            )
            print(percentage_difference)
            print(self.closest_object_distance)
            print(self.previous_closest_object_distance)

            # Determine if the object is moving or static based on the threshold
            if percentage_difference > self.speed_distance_threshold:
                object_state = "Moving"
            else:
                object_state = "Static"

            print(f"Closest Object State: {object_state}")

        # Update the previous closest object state for the next frame
        self.previous_closest_object_distance = self.closest_object_distance
        self.previous_closest_object_class = self.closest_object_class

    def make_decisions(self):
        # Decision-making logic based on the current state for all objects

        for distance, obj_class, bbox in zip(distances, obj_classes, bboxes):
            # Update the state for the current object
            self.closest_object_distance = distance
            self.closest_object_class = obj_class
            self.closest_object_bbox = bbox

            # Print parameters for the current object
            print(f"Object: {obj_class}")
            print(f"Distance: {distance}")
            print(f"BBox: {bbox}")
            print("Making decision...")

            # Check if there is an obstacle within a safe distance
            if distance < 2.0:  # Adjust the threshold as needed
                if obj_class == "car":
                    # Check if the object is a moving car
                    if self.is_moving_car():
                        self.avoid_collision()
                    else:
                        self.stop_and_wait()
                elif obj_class == "person":
                    self.stop_and_yield_to_pedestrian()

            # Check for changes in direction
            if self.is_direction_change_needed():
                self.adjust_direction()

        # Track the state of the closest object
        self.track_closest_object_state()

    def is_moving_car(self):
        # Logic to determine if the closest object is a moving car
        # You may use additional information or machine learning models for this
        return True  # Placeholder, replace with actual logic

    def avoid_collision(self):
        # Logic to avoid collision with a moving car
        # Implement your own collision avoidance strategy
        print("Collision detected! Taking evasive action.")

    def stop_and_wait(self):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        print("Stopping and waiting for the obstacle.")

    def stop_and_yield_to_pedestrian(self):
        # Logic to stop and yield to pedestrians
        # Implement your own strategy for yielding to pedestrians
        print("Stopping and yielding to pedestrians.")

    def is_direction_change_needed(self):
        # Placeholder logic, replace with your own
        # Check if the direction needs to be changed based on some criteria
        return True

    def adjust_direction(self):
        # Placeholder logic, replace with your own
        # Implement logic to adjust the direction of the robotic car
        print("Adjusting direction.")

# Example usage:
decision_maker = RoboticCarDecisionMaker()

# Example arrays for distances, obj_classes, and bboxes
distances = [1.5, 2.0, 3.0]  # Replace with actual distances
obj_classes = ["car", "person", "car"]  # Replace with actual classes
bboxes = [((0, 0), (10, 10)), ((5, 5), (15, 15)), ((2, 2), (12, 12))]  # Replace with actual bounding boxes

# Make decisions based on the updated state for all objects
decision_maker.make_decisions()

class RoboticCarDecisionMaker:
    def __init__(self):
        # Initialize some variables for the current state
        self.closest_object_distance = float('inf')  # Start with a large distance
        self.closest_object_class = None
        self.closest_object_bbox = None
        self.current_direction = "straight"  # Start with a default direction
        self.previous_closest_object_distance = 1.498
        self.previous_closest_object_class = 'car'
        self.speed_distance_threshold = 0.05  # 5% threshold for speed difference

    def update_state(self, distances, obj_classes, bboxes):
        # Update the state with the latest object detection information
        objects = zip(distances, obj_classes, bboxes)
        sorted_objects = sorted(objects, key=lambda x: x[0])  # Sort based on distance
        self.closest_object_distance, self.closest_object_class, self.closest_object_bbox = sorted_objects[0]

    def track_closest_object_state(self):
        # Track the state of the closest object over consecutive frames
        if (
            self.previous_closest_object_distance is not None
            and self.previous_closest_object_class == self.closest_object_class
        ):
            # Calculate the percentage difference in distances
            percentage_difference = abs(
                (self.closest_object_distance - self.previous_closest_object_distance) / self.previous_closest_object_distance
            )
            print(self.previous_closest_object_distance)
            print(self.closest_object_distance)
            print(percentage_difference)
            # Determine if the object is moving or static based on the threshold
            if percentage_difference > self.speed_distance_threshold:
                object_state = "Moving"
            else:
                object_state = "Static"

            print(f"Closest Object State: {object_state}")



        # print(self.previous_closest_object_distance)
        # print(self.closest_object_distance)
        # print(self.percentage_difference)
        # Update the previous closest object state for the next frame
        self.previous_closest_object_distance = self.closest_object_distance
        self.previous_closest_object_class = self.closest_object_class
        print(self.previous_closest_object_distance)

    def make_decisions(self):
        # Decision-making logic based on the current state for all objects
        it = 0
        for distance, obj_class, bbox in zip(distances, obj_classes, bboxes):
            # Update the state for the current object
            self.closest_object_distance = distance
            self.closest_object_class = obj_class
            self.closest_object_bbox = bbox

            # Print parameters for the current object
            print(f"Object: {obj_class}")
            print(f"Distance: {distance}")
            print(f"BBox: {bbox}")
            print("Making decision...")

            # Check if there is an obstacle within a safe distance
            if distance < 2.0:  # Adjust the threshold as needed
                if obj_class == "car":
                    # Check if the object is a moving car
                    if self.is_moving_car():
                        self.avoid_collision()
                    else:
                        self.stop_and_wait()
                elif obj_class == "person":
                    self.stop_and_yield_to_pedestrian()

            # Check for changes in direction
            if self.is_direction_change_needed():
                self.adjust_direction()

        # Track the state of the closest object
            if it == 0:
                self.track_closest_object_state()

            it += 1

    def is_moving_car(self):
        # Logic to determine if the closest object is a moving car
        # You may use additional information or machine learning models for this
        return True  # Placeholder, replace with actual logic

    def avoid_collision(self):
        # Logic to avoid collision with a moving car
        # Implement your own collision avoidance strategy
        print("Collision detected! Taking evasive action.")

    def stop_and_wait(self):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        print("Stopping and waiting for the obstacle.")

    def stop_and_yield_to_pedestrian(self):
        # Logic to stop and yield to pedestrians
        # Implement your own strategy for yielding to pedestrians
        print("Stopping and yielding to pedestrians.")

    def is_direction_change_needed(self):
        # Placeholder logic, replace with your own
        # Check if the direction needs to be changed based on some criteria
        return True

    def adjust_direction(self):
        # Placeholder logic, replace with your own
        # Implement logic to adjust the direction of the robotic car
        print("Adjusting direction.")

# Example usage:
decision_maker = RoboticCarDecisionMaker()

# Example arrays for distances, obj_classes, and bboxes
distances = [1.5, 2.0, 3.0]  # Replace with actual distances
obj_classes = ["car", "person", "car"]  # Replace with actual classes
bboxes = [((0, 0), (10, 10)), ((5, 5), (15, 15)), ((2, 2), (12, 12))]  # Replace with actual bounding boxes

# Make decisions based on the updated state for all objects
decision_maker.make_decisions()

class RoboticCarDecisionMaker:
    def __init__(self):
        # Initialize some variables for the current state
        self.closest_object_distance = float('inf')  # Start with a large distance
        self.closest_object_class = None
        self.closest_object_bbox = None
        self.current_direction = "straight"  # Start with a default direction
        self.previous_closest_object_distance = 1.22
        self.previous_closest_object_class = 'person'
        self.speed_distance_threshold = 0.02  # 5% threshold for speed difference

    # def update_state(self, distances, obj_classes, bboxes):
    #     # Update the state with the latest object detection information
    #     objects = zip(distances, obj_classes, bboxes)
    #     sorted_objects = sorted(objects, key=lambda x: x[0])  # Sort based on distance
    #     self.closest_object_distance, self.closest_object_class, self.closest_object_bbox = sorted_objects[0]


    def update_state(self, distances, obj_classes, bboxes):
        # Update the state with the latest object detection information
        objects = zip(distances, obj_classes, bboxes)
        sorted_objects = sorted(objects, key=lambda x: x[0])  # Sort based on distance
        self.closest_object_distance, self.closest_object_class, self.closest_object_bbox = sorted_objects[0]

        # Return the sorted values
        return sorted(distances), sorted(obj_classes), sorted(bboxes, key=lambda x: x[0][0])

    def track_closest_object_state(self):
        # Track the state of the closest object over consecutive frames
        fps = 15
        t = 1 / fps
        v = 0.02 # meter per second
        if (
            self.previous_closest_object_distance is not None
            and self.previous_closest_object_class == self.closest_object_class
        ):
            # Calculate the percentage difference in distances
            percentage_difference = abs(
                ((self.closest_object_distance + (t*v)) - self.previous_closest_object_distance) / self.previous_closest_object_distance
            )
            print(self.previous_closest_object_distance)
            print(self.closest_object_distance)
            print(percentage_difference)
            # Determine if the object is moving or static based on the threshold
            if percentage_difference > self.speed_distance_threshold:
                object_state = "Moving"
            else:
                object_state = "Static"

            print(f"Closest Object State: {object_state}")
            # self.make_decision_for_object(self.closest_object_class, object_state)
        else:
          object_state = None
        # Update the previous closest object state for the next frame
        self.previous_closest_object_distance = self.closest_object_distance
        self.previous_closest_object_class = self.closest_object_class
        print(self.previous_closest_object_distance)

        return object_state

    def make_decisions(self, distances, obj_classes, bboxes, direction='straight'):
        # Decision-making logic based on the current state for all objects

        distances, obj_classes, bboxes = self.update_state(distances, obj_classes, bboxes)


        width_frame = 720 # assuming width of camera frame as 720pixels horizontal
        if direction=='straight':
            direction = 's'
        else:
          self.adjust_direction(direction)

        it = 0
        for distance, obj_class, bbox in zip(distances, obj_classes, bboxes):
            # Update the state for the current object
            self.closest_object_distance = distance
            self.closest_object_class = obj_class
            self.closest_object_bbox = bbox


            # # Check if there is an obstacle within a safe distance
            # if distance < 2.0:  # Adjust the threshold as needed
            #     if obj_class == "car":
            #         # Check if the object is a moving car
            #         if self.is_moving_car(obj_class):
            #             self.avoid_collision(obj_class)
            #         else:
            #             self.stop_and_wait(obj_class)
            #     elif obj_class == "person":
            #         self.stop_and_yield_to_pedestrian(obj_class)
            #     # Add similar checks for other object classes

            # Check for changes in direction
            # if direction=='straight':
            #     direction = 's'

            # else:
            #     self.adjust_direction(direction)

            # Track the state of the closest object for the first object in the array
            if distance < 2.0 and it == 0:
                print("Main decision as this is the closest object")
                obj_state = self.track_closest_object_state()
                # Print parameters for the closest object
                print(f"Object: {obj_class}")
                print(f"Distance: {distance}")
                print(f"BBox: {bbox}")
                x1 = bbox[0][0]
                x2 = bbox[1][0]
                length = abs(x2 - x1)
                print(f"Object width: {length}")

                print("Making decision...")
                self.make_decision_for_object(obj_class,obj_state,length, distance)

            it += 1

    # def is_moving_car(self, obj_class):
    #     # Logic to determine if the closest object is a moving car
    #     # You may use additional information or machine learning models for this
    #     print(f"Checking if {obj_class} is a moving car...")
    #     return True  # Placeholder, replace with actual logic

    def make_decision_for_object(self, obj_class, object_state, length, distance):
        # Make decisions based on the class and state of the object
        if obj_class == "car":
            if object_state == "Moving":
                self.reduce_speed_MoveBehindObject(obj_class, distance)
            else:
                self.overtake_right(obj_class,length)

        # Add similar logic for other object classes

        elif obj_class == "bus":
            if object_state == "Moving":
                self.reduce_speed_MoveBehindObject(obj_class, distance)
            else:
                self.overtake_right(obj_class,length)


        elif obj_class == "bicycle":
            if object_state == "Moving":
                self.reduce_speed_MoveBehindObject(obj_class, distance)
            else:
                self.overtake_right(obj_class,length)


        elif obj_class == "motorcycle":
            if object_state == "Moving":
                self.reduce_speed_MoveBehindObject(obj_class, distance)
            else:
                self.overtake_right(obj_class,length)


        elif obj_class == "truck":
            if object_state == "Moving":
                self.reduce_speed_MoveBehindObject(obj_class, distance)
            else:
                self.overtake_right(obj_class,length)


        elif obj_class == "rider":
            if object_state == "Moving":
                self.stop_and_wait(obj_class)
            else:
                # Implement logic for a stationary person
                self.stop_hornForClearance(obj_class)


        elif obj_class == "pedestrian":
            if object_state == "Moving":
                self.stop_and_wait(obj_class)
            else:
                # Implement logic for a stationary person
                self.stop_hornForClearance(obj_class)


        elif obj_class == "traffic light":
            if object_state == "Moving":
                self.stop_and_wait(obj_class)
            else:
                # Implement logic for a stationary person
                self.stop_hornForClearance(obj_class)


        elif obj_class == "traffic sign":
            if object_state == "Moving":
                self.stop_and_wait(obj_class)
            else:
                # Implement logic for a stationary person
                self.stop_hornForClearance(obj_class)


    def reduce_speed_MoveBehindObject(self, obj_class, distance):
        # Logic to avoid collision with a moving car
        # Implement your own collision avoidance strategy
        reduce_speed = 1
        if distance > 1:
           reduce_speed = 1
        else:
           reduce_speed = 2
        print(f"Collision detected with {obj_class}! Taking evasive action. Use reduce speed function {reduce_speed}")

    def overtake_right(self, obj_class, length):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        o_t_ref = 0.5
        width_frame = 720 # assuming width of camera frame as 720pixels horizontal

        sc = length/width_frame
        if sc > o_t_ref:
          os = 'large overtake'
        else:
          os = 'small overtake'

        print(f"Overtake from right lane for object {obj_class} with camera width {length} and overtake should be {os}.")


    def move_left_after_overtake(self, obj_class, length):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        print(f"Overtake from right lane for object {obj_class} with camera width {length}.")


    def stop_and_wait(self, obj_class):
        # Logic to stop and wait when there is a static obstacle
        # Implement your own strategy for stopping and waiting
        print(f"Stopping and waiting for {obj_class}.")

    def stop_hornForClearance(self, obj_class):
        # Logic to stop and yield to pedestrians
        # Implement your own strategy for yielding to pedestrians
        print(f"Stopping and buzzing to {obj_class}.")

    def is_direction_change_needed(self):
        # Placeholder logic, replace with your own
        # Check if the direction needs to be changed based on some criteria
        return True

    def adjust_direction(self, direction):
        # Placeholder logic, replace with your own
        if direction == 'left':
          direction='l'
        elif direction == 'right':
          direction='r'
        else:
          direction = 's'
        # Implement logic to adjust the direction of the robotic car
        print(f"Adjusting direction to {direction}")

# Example usage:
decision_maker = RoboticCarDecisionMaker()

# Example arrays for distances, obj_classes, and bboxes
distances = [1.5, 1.2, 3.0]  # Replace with actual distances
obj_classes = ["car", "person", "car"]  # Replace with actual classes
bboxes = [((0, 0), (10, 10)), ((5, 5), (15, 15)), ((2, 2), (12, 12))]  # Replace with actual bounding boxes
direction = 'left'

# Make decisions based on the updated state for all objects
decision_maker.make_decisions(distances, obj_classes, bboxes, direction)

