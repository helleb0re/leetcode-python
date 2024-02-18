from typing import List


# the main idea is to the farthest car can ONLY stop cars behind

# if the farthest car have time > than the nearest car that means
# it will come later than the nearest car and they will be collided (car fleet)


# if the farthest car (or cars) reaches destination earlier than
# the remainders, we need define new the farthest car that didn't finish
# and repeat the action which was described before
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars_info = sorted(((pos, s) for pos, s in zip(position, speed)), reverse=True)
    buffer = [cars_info[0]]
    for car_info in cars_info[1:]:
        buff_car_pos, buff_car_speed = buffer[-1]
        buff_car_time = (target - buff_car_pos) / buff_car_speed

        curr_car_pos, curr_car_speed = car_info
        curr_car_time = (target - curr_car_pos) / curr_car_speed

        if curr_car_time > buff_car_time:
            buffer.append(car_info)

    return len(buffer)


if __name__ == "__main__":
    assert carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert carFleet(10, [3], [3]) == 1
    assert carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
