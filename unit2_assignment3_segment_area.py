{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area of minor segment = 28.53975000004401\n",
      "Area of major segment = 285.6192499996039\n"
     ]
    }
   ],
   "source": [
    "import math   \n",
    "pi = 3.14159\n",
    "def area_of_segment(radius, angle): \n",
    "   \n",
    "    area_of_sector = pi * (radius * radius) * (angle / 360) \n",
    " \n",
    "    area_of_triangle = 1 / 2 * (radius * radius)*math.sin((angle * pi) / 180) \n",
    "  \n",
    "    return area_of_sector - area_of_triangle; \n",
    "radius = 10.0\n",
    "angle = 90.0\n",
    "print(\"Area of minor segment =\", \n",
    "       area_of_segment(radius, angle)) \n",
    "print(\"Area of major segment =\", \n",
    "      area_of_segment(radius, (360 - angle))) \n",
    "        \n",
    "       \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
