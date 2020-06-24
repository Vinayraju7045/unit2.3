{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the length of each side of Polygon (in meters): 78\n",
      "Enter the number of sides: 6\n",
      "The area of Polygon is 15806.70 \n"
     ]
    }
   ],
   "source": [
    "from math import tan,pi\n",
    " \n",
    "GRAVITY = 9.8  \n",
    " \n",
    "length  = float(input(\"Enter the length of each side of Polygon (in meters): \"))\n",
    "number  = int(input(\"Enter the number of sides: \"))\n",
    " \n",
    "area = (number * length ** 2)/(4 * tan(pi/number))\n",
    " \n",
    "print(\"The area of Polygon is %.2f \" % area)"
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
