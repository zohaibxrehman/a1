"""CSC148 Assignment 1 - Making Music

=== CSC148 Summer 2019 ===
Department of Computer Science,
University of Toronto

=== Module Description ===

This file contains classes that describe sound waves, instruments that play
these sounds and a function that plays multiple instruments simultaneously.

As discussed in the handout, you may not change any of the public behaviour 
(attributes, methods) given in the starter code, but you can definitely add 
new attributes, functions, classes and methods to complete your work here.

"""
from __future__ import annotations
import typing
import csv
import numpy
from helpers import play_sound, play_sounds, make_sine_wave_array


class SimpleWave:
    """ TODO: write a docstring for this class """
    def __init__(self, frequency: int, 
                 duration: float, amplitude: float) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __eq__(self, other: SimpleWave) -> bool:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __ne__(self, other: SimpleWave) -> bool:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __add__(self, 
                other: ANYWAVE) -> ComplexWave:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body


class ComplexWave:
    """ TODO: write a docstring for this class """
    def __init__(self, waves: typing.List[SimpleWave]) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __add__(self, 
                other: ANYWAVE) -> ComplexWave:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def complexity(self) -> int:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_waves(self) -> typing.List[SimpleWave]:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body       

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body 

    def simplify(self) -> None:
        """ TODO: write a docstring for this method 
            REMEMBER: this is not a required part of the assignment 
        """
        pass  # TODO: finish this method body 


class Note:
    """ TODO: write a docstring for this class """
    amplitude: float
    
    def __init__(self, waves: typing.List[ANYWAVE]) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __add__(self, other: Note) -> Note:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_waves(self) -> typing.List[ANYWAVE]:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body


class SawtoothWave:
    """ TODO: write a docstring for this class """
    def __init__(self, frequency: int, 
                 duration: float, amplitude: float) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __add__(self, 
                other: ANYWAVE) -> ComplexWave:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def complexity(self) -> int:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_waves(self) -> typing.List[SimpleWave]:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body       

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body 

    def simplify(self) -> None:
        """ TODO: write a docstring for this method 
            REMEMBER: this is not a required part of the assignment 
        """
        pass  # TODO: finish this method body 


class SquareWave:
    """ TODO: write a docstring for this class """
    def __init__(self, frequency: int, 
                 duration: float, amplitude: float) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __add__(self, 
                other: ANYWAVE) -> ComplexWave:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def complexity(self) -> int:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_waves(self) -> typing.List[SimpleWave]:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body       

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body 

    def simplify(self) -> None:
        """ TODO: write a docstring for this method 
            REMEMBER: this is not a required part of the assignment 
        """
        pass  # TODO: finish this method body 


class Rest:
    """ TODO: write a docstring for this class """
    def __init__(self, duration: float) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def __add__(self, 
                other: ANYWAVE) -> ComplexWave:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def complexity(self) -> int:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_waves(self) -> typing.List[SimpleWave]:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body       

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body 

    def simplify(self) -> None:
        """ TODO: write a docstring for this method 
            REMEMBER: this is not a required part of the assignment 
        """
        pass  # TODO: finish this method body 


class StutterNote:
    """ TODO: write a docstring for this class """
    amplitude: float
    
    def __init__(self, frequency: int, 
                 duration: float, amplitude: float) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body 

    def __add__(self, other: Note) -> Note:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_waves(self) -> typing.List[ANYWAVE]:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

class Baliset:
    """ TODO: write a docstring for this class """
    def __init__(self) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def next_notes(self, 
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body


class Holophonor:
    """ TODO: write a docstring for this class """
    def __init__(self) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def next_notes(self, 
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body


class Gaffophone:
    """ TODO: write a docstring for this class """
    def __init__(self) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def get_duration(self) -> float:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def next_notes(self, 
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body

    def play(self) -> numpy.ndarray:
        """ TODO: write a docstring for this method """
        pass  # TODO: finish this method body


def play_song(song_file: str, beat: float) -> None:
    """ TODO: write a docstring for this function """
    pass  # TODO: finish this function body    


# This is a custom type for type annotations that 
# refers to any of the following classes (do not 
# change this code)
ANYWAVE = typing.TypeVar('ANYWAVE', 
                         SimpleWave, 
                         ComplexWave, 
                         SawtoothWave, 
                         SquareWave, 
                         Rest)

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['helpers', 
                                                  'typing', 
                                                  'csv', 
                                                  'numpy'],
                                'disable': ['E9997']})
