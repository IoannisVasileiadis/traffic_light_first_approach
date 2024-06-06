import pygame
import sys


class TrafficLightCars:
    RED_INTERVAL = 4000 # Define the red interval to 4000 milliseconds
    YELLOW_INTERVAL = 1000 # Define the yellow interval to 1000 milliseconds
    GREEN_INTERVAL = 3000 # Define the green interval to 3000 milliseconds

    def __init__(self, red_interval=RED_INTERVAL,rotated=True, initial_state="red"):
        # Load traffic light images
        self.red_light = pygame.image.load('images/red_car_traffic_light.png')
        self.yellow_light = pygame.image.load('images/yellow_car_traffic_light.png')
        self.green_light = pygame.image.load('images/green_car_traffic_light.png')

        if rotated: # Check if the rotated flag is True
            self.red_light = pygame.transform.rotate(self.red_light, 270)
            self.yellow_light = pygame.transform.rotate(self.yellow_light, 270)
            self.green_light = pygame.transform.rotate(self.green_light, 270)

        # Initialize the state of the traffic light
        if initial_state not in ["red", "yellow", "green"]:
            raise ValueError("Invalid initial state. State must be one of 'red', 'yellow', or 'green'")
        self.state = initial_state

        # Initialize the start time
        self.start_time = pygame.time.get_ticks() # Get current time in milliseconds
        self.interval = red_interval # Set the interval to the red interval

    # Check state and draw the lights
    def draw(self, screen, position):
        if self.state == "red":
            screen.blit(self.red_light, position)
        elif self.state == "yellow":
            screen.blit(self.yellow_light, position)
        elif self.state == "green":
            screen.blit(self.green_light, position)

    # Check the time that has been passed since program initialization
    def check_time_has_passed(self):
        current_time = pygame.time.get_ticks() # Get a time stamp in milliseconds
        if current_time - self.start_time >= self.interval:
            self.switch_light() # Switch the status of the light

    def get_light_state(self):
        return self.state # Return the current state of the light

    # Function to switch lights based on state
    def switch_light(self,red_interval=RED_INTERVAL, yellow_interval=YELLOW_INTERVAL, green_interval=GREEN_INTERVAL):
        if self.state == "red": # Check if the state of light is red
            self.state = "green"   # Switch to green
            self.interval = green_interval
        elif self.state == "green": # Check if the state of light is green
            self.state = "yellow"  # Switch to yellow
            self.interval = yellow_interval
        elif self.state == "yellow": # Check if the state of light is yellow
            self.state = "red"    # Switch to red
            self.interval = red_interval
        self.start_time = pygame.time.get_ticks() # Reset the start time


def main():

    pygame.init()

    # Set the dimensions of the window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))


    # Create an instance of TrafficLightCars for the first traffic light
    traffic_light1 = TrafficLightCars(initial_state="green", red_interval=4000)

    # Create an instance of TrafficLightCars for the second traffic light
    traffic_light2 = TrafficLightCars(rotated=False, initial_state="red", red_interval=5000)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Check if the time has passed and switch the light

        traffic_light1.check_time_has_passed()
        traffic_light2.check_time_has_passed()

        #Draw the first traffic light at a position
        traffic_light1.draw(screen, (width//2, height//2))

        #Draw the second traffic light at a different position
        traffic_light2.draw(screen, (width//2+100, height//2+100))

        pygame.display.flip()

if __name__ == "__main__":
    main()
