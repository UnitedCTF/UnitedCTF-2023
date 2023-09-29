#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define NUMBER_OF_DESTINATIONS 27
char* DESTINATIONS[NUMBER_OF_DESTINATIONS] = {
    "Port_Royal,17.937639,-76.843667",
    "Nassau,25.0326326,-77.4482922",
    "Ocracoke_Island,35.1293949,-75.9120657",
    "Tortuga,20.079612,-72.764167",
    "New_Providence,25.0248173,-77.2741612",
    "Libertalia,-17.7449304,45.8230733",
    "Cartagena,12.1659652,-74.5389643",
    "Havana,23.1276627,-82.3472504",
    "Saint-Malo,48.6463258,-2.0272343",
    "Maracaibo,10.6864087,-71.6338542",
    "Portobelo,9.5496331,-79.6548271",
    "Charleston,32.5496099,-74.7963471",
    "Madagascar,-17.7449304,45.8230733",
    "Algiers,36.6967742,3.0098215",
    "Bristol,51.7649422,-1.8982978",
    "Veracruz,19.8021044,-97.4635989",
    "Galveston,30.188985,-99.2206606",
    "Port_Saint_Joe,29.7785999,-85.3185395",
    "Bridgetown,13.3143251,-60.1617691",
    "Lagos,5.4956974,1.0415702",
    "La_Tortuga,11.0121783,-65.3918381",
    "Dunkirk,51.1761664,1.7401102",
    "Plymouth,50.3860968,-4.2049699",
    "Belize_City,18.0278754,-88.6404272",
    "Cape_Town,-33.8601301,17.5215051",
    "Marseille,43.2804407,5.2982481",
    "Santiago_de_Cuba,20.0244119,-75.8672963"
};
int SAIL_LEVEL = 0;
const char* SAIL_LEVELS[5] = {
    "no sail",
    "storm sail",
    "reefed sail",
    "half sail",
    "full sail"
};
int FIRE_AT_SIGHT = 0;
double CURRENT_LATITUDE = 20.086588;
double CURRENT_LONGITUDE = -72.822861;

int set_anchor(int anchor_down) {
    if (anchor_down) {
        printf("Arrr, the anchor be up and ready for adventure on the high seas, me hearties!\n");
        return 1;
    }
    else {
        printf("Arrr, the anchor be down, me matey!\n");
        return 0;
    }
}

int set_sail(int sail_level) {
    SAIL_LEVEL = sail_level;
    if (SAIL_LEVEL == sail_level) {
        printf("Sail set to %s\n", SAIL_LEVELS[SAIL_LEVEL]);
        return 0;
    }
    return 1;
}

void sail(double destination_latitude, double destination_longitude, int speed) {
    printf("\nTrack our position, Captain:\n");
    double distance_x;
    double distance_y;
    while ((CURRENT_LATITUDE != destination_latitude) || (CURRENT_LONGITUDE != destination_longitude)) {
        printf("(%f, %f)\n", CURRENT_LATITUDE, CURRENT_LONGITUDE);
        distance_y = (destination_latitude - CURRENT_LATITUDE);
        distance_x = (destination_longitude - CURRENT_LONGITUDE);

        sleep(3);
        float parcoured_distance = (float)speed / 10000;

        if (distance_x > 0.0) {
            if ((parcoured_distance) > distance_x) {
                CURRENT_LONGITUDE = destination_longitude;
            }
            else {
                CURRENT_LONGITUDE += parcoured_distance;
            }
        }
        else if (distance_x < 0.0) {
            if ((parcoured_distance) > -1 * distance_x ) {
                CURRENT_LONGITUDE = destination_longitude;
            }
            else {
                CURRENT_LONGITUDE -= parcoured_distance;
            }
        }

        if (distance_y > 0.0) {
            if ((parcoured_distance) > distance_y) {
                CURRENT_LATITUDE = destination_latitude;
            }
            else {
                CURRENT_LATITUDE += parcoured_distance;
            }
        }
        else if (distance_y < 0.0) {
            if ((parcoured_distance) > -1 * distance_y ) {
                CURRENT_LATITUDE = destination_latitude;
            }
            else {
                CURRENT_LATITUDE -= parcoured_distance;
            }
        }
    }
    printf("(%f, %f)\n", CURRENT_LATITUDE, CURRENT_LONGITUDE);
}

void set_coordinates(int destination, int fire_at_sight, int speed) {
    if (fire_at_sight) {
        FIRE_AT_SIGHT = 1;
    }

    char * destination_infos = DESTINATIONS[destination];
    const char * latitude_start = strchr(destination_infos, ',') + 1;
    const char * longitude_start = strrchr(destination_infos, ',') + 1;
    char destination_latitude[20];
    char destination_longitude[20];

    size_t latitude_length = longitude_start - latitude_start - 1;
    strncpy(destination_latitude, latitude_start, latitude_length);
    destination_latitude[latitude_length] = '\0';
    strcpy(destination_longitude, longitude_start);
    printf("Coordinates set, me matey! We are set to sail!\n");

    sail(atof(destination_latitude), atof(destination_longitude), speed);
}

int main(int argc, char** argv) {
    if (argc < 4) {
        return -1;
    }
    int speed = atoi(argv[1]);
    int destination = atoi(argv[2]);
    int fire_at_sight = atoi(argv[3]);
    if ((speed < 0) || (5 <= speed)) {
        return 1;
    }
    if ((destination < 0) || (NUMBER_OF_DESTINATIONS <= destination)) {
        return 2;
    }
    if (!set_anchor(1)) {
        return 0;
    }
    set_sail(speed);
    set_coordinates(destination, fire_at_sight, speed);
}