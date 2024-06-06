import pygame
import sys

class TrafficLightCars_2:
    TURNED_OFF_INTERVAL = 1000 # Define the interval for the turned_off state to 1000 milliseconds
    YELLOW_INTERVAL = 1000 # Define the interval for the yellow state to 1000 milliseconds

    def __init__(self, turned_off_interval=TURNED_OFF_INTERVAL,rotated=True,initial_state="turned_off"):
        # Load the traffic light images
        self.turned_off_light = pygame.image.load('images/turned_off_car_traffic_light.png')
        self.yellow_light = pygame.image.load('images/yellow_car_traffic_light.png')

        if rotated: # Check if the rotated flag is True
            self.turned_off_light = pygame.transform.rotate(self.turned_off_light, 270)
            self.yellow_light = pygame.transform.rotate(self.yellow_light, 270)

    # Initialize the state of the traffic light
        if initial_state not in ["turned_off", "yellow"]:
            raise ValueError("Invalid initial state. State must be one of 'turned_off' or 'yellow'")
        self.state = initial_state

        # Initialize start time
        self.start_time = pygame.time.get_ticks() # Get current time in milliseconds
        self.interval = turned_off_interval # Set the interval to the turned_off interval

    # Check state and draw the lights
    def draw(self, screen, position):
        if self.state == "turned_off":
            screen.blit(self.turned_off_light, position)
        elif self.state == "yellow":
            screen.blit(self.yellow_light, position)

    #Check how much time has been passed since program initialization
    def check_time_has_passed(self):
        current_time = pygame.time.get_ticks() # Get the current time in milliseconds
        if current_time - self.start_time >= self.interval:
            self.switch_light() # Switch the light

    def get_light_state(self):
        return self.state # Return the current state of the light

   #function to switch lights based on state
    def switch_light(self,turned_off_interval=TURNED_OFF_INTERVAL, yellow_interval=YELLOW_INTERVAL):
        if self.state == "turned_off": # Check if the state of light is turned_off
            self.state = "yellow"   # Switch to yellow
            self.interval = yellow_interval
        elif self.state == "yellow":
            self.state = "turned_off"  # Switch to turned_off
            self.interval = turned_off_interval
        self.start_time = pygame.time.get_ticks() # Reset the start time

def main():

    pygame.init()

    # Set the dimensions of the window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))


    # Create an instance of TrafficLightCars for the first traffic light
    traffic_light1 = TrafficLightCars_2()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Check if the time has passed and switch the light

        traffic_light1.check_time_has_passed()

        # Draw the first traffic light at a position
        traffic_light1.draw(screen, (width//2, height//2))

        pygame.display.flip()

if __name__ == "__main__":
    main()
