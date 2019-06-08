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
    """


    === Attributes ===
    freq: frequency of the simple wave
    duration: duration of the simple wave
    amp: amplitude of the simple wave
    """
    freq: int #FIXME WHAT IS TYPE? INT OR FLOAT
    duration: float
    amp: float

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the simple wave.
        """
        self.freq = frequency
        self.duration = duration
        self.amp = amplitude
        #FIXME WHAT IS DURATION FOR?

    def __eq__(self, other: SimpleWave) -> bool:
        """Return true if this simple wave and other simple wave are equal.
        """
        return (self.freq == other.freq and self.duration == other.duration and
                self.amp == other.amp)

    def __ne__(self, other: SimpleWave) -> bool:
        """Return true if this simple wave and other simple wave are not
        equal.
        """
        return not self == other

    def __add__(self,
                other: ANYWAVE) -> ComplexWave:
        """add"""
        return ComplexWave([self, other])
        #FIXME sum of two simple waves.

    def get_duration(self) -> float:
        """Return duration of a SimpleWave instance in seconds."""
        return self.duration

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents a simple sine wave based on the
         frequency and duration of the simple wave.
         """
        return make_sine_wave_array(self.freq, self.duration)


class ComplexWave:
    """


    === Attributes ===
    waves: list of simple waves that build this complex wave
    """
    def __init__(self, waves: typing.List[SimpleWave]) -> None:
        """Initialises the complex wave"""
        self.waves = waves

    def __add__(self,
                other: ANYWAVE) -> ComplexWave:
        """Return the sum of a complex wave and another wave."""
        if isinstance(other, SimpleWave):
            return ComplexWave(self.waves + [other])
        elif isinstance(other, ComplexWave):
            return ComplexWave(self.waves + other.waves)

    def complexity(self) -> int:
        """Return the coplexity of the complex wave."""
        return len(self.waves)

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents a wave based on the additive
        synthesis of its simple waves.
        """
        if len(self.waves) != 0:
            arr = self.waves[0].play()
            for wave in self.waves[1:]:
                arr = arr + wave.play()
                #  numpy.add?
            if arr.max() != 0:
                return arr / arr.max()
            else:
                return arr

    def get_waves(self) -> typing.List[SimpleWave]:
        """Return a list of SimpleWave instances that can be added together
        to represent a ComplexWave instance."""
        return self.waves

    def get_duration(self) -> float:
        """Return the duration of the complex wave. This duration is the maximum
         duration of its simple waves"""
        lst = []
        for wave in self.waves:
            lst.append(wave.duration)
        return max(lst)

    def simplify(self) -> None:
        """ TODO: write a docstring for this method
            REMEMBER: this is not a required part of the assignment
        """
        pass  # TODO: finish this method body


class Note:
    """

    === Attributes ===
    amplitude: amplitude of the Note
    waves: list of simple/complex waves that build this note
    """
    amplitude: float
    waves: list

    def __init__(self, waves: typing.List[ANYWAVE]) -> None:
        """Initialise the Note.
        """
        self.amplitude = 1
        self.waves = waves

    def __add__(self, other: Note) -> Note:
        """Return the sum of this note and the other note. This Note instance,
        when played, should sound exactly the same as playing the first Note
        instance followed by the second with no pause in between.
        The amplitude of the result will be the greatest amplitude of the two
        combined Note instances.
        """
        beat = Note(self.waves + other.waves)
        beat.amplitude = max(self.amplitude, other.amplitude)
        return beat

    def get_waves(self) -> typing.List[ANYWAVE]:
        """Return a list of waves (ComplexWave or SimpleWave instances) that
        represent the waves that, if played in order with no pauses in between,
        would sound exactly like playing the Note instance, that is, the
        components of this Note.
        """
        return self.waves

    def get_duration(self) -> float:
        """Return the duration of the note."""
        dur = 0
        for wave in self.waves:
            dur = dur + wave.get_duration()
        return dur

    def play(self) -> numpy.ndarray:
        """ """
        if len(self.waves) != 0:
            arr = self.waves[0].play()
            for wave in self.waves[1:]:
                arr = numpy.append(arr, wave.play())
                #  FIXME is append the way?
            return arr * self.amplitude


class SawtoothWave(ComplexWave):
    """

    === Attributes ===
    waves: list of simple waves that build this complex wave
    """
    waves: list

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the sawtooth wave.
        """
        self.waves = []
        for k in range(1, 11):
            self.waves.append(SimpleWave(k * frequency, duration,
                                         amplitude / k))

    # def __add__(self,
    #             other: ANYWAVE) -> ComplexWave:
    #     """ """

    # def complexity(self) -> int:
    #     """ """
    #     return len()

    # def play(self) -> numpy.ndarray:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body

    # def get_waves(self) -> typing.List[SimpleWave]:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body

    # def get_duration(self) -> float:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body

    # def simplify(self) -> None:
    #     """ TODO: write a docstring for this method
    #         REMEMBER: this is not a required part of the assignment
    #     """
    #     pass  # TODO: finish this method body


class SquareWave(ComplexWave):
    """

    === Attributes ===
    waves: list of simple waves that build this complex wave
    """
    waves: list

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the sawtooth wave.
        """
        self.waves = []
        for k in range(1, 11):
            self.waves.append(SimpleWave((2 * k - 1) * frequency, duration,
                                         amplitude / (2 * k - 1)))

    # def __add__(self,
    #             other: ANYWAVE) -> ComplexWave:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def complexity(self) -> int:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def play(self) -> numpy.ndarray:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def get_waves(self) -> typing.List[SimpleWave]:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def get_duration(self) -> float:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def simplify(self) -> None:
    #     """ TODO: write a docstring for this method
    #         REMEMBER: this is not a required part of the assignment
    #     """
    #     pass  # TODO: finish this method body


class Rest(ComplexWave):
    """

    """
    waves: list

    def __init__(self, duration: float) -> None:
        """Initialise the rest"""
        ComplexWave.__init__(self, [SimpleWave(0, duration, 0)])
    # def __add__(self,
    #             other: ANYWAVE) -> ComplexWave:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def complexity(self) -> int:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def play(self) -> numpy.ndarray:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def get_waves(self) -> typing.List[SimpleWave]:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def get_duration(self) -> float:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def simplify(self) -> None:
    #     """ TODO: write a docstring for this method
    #         REMEMBER: this is not a required part of the assignment
    #     """
    #     pass  # TODO: finish this method body


class StutterNote(Note):
    """

    === Attributes ===
    amplitude: amplitude of the Note
    waves: list of simple/complex waves that build this note
    """
    amplitude: float
    waves: list

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the stutter note.
        """
        waves = []
        for i in range(20 * duration):
            waves.append(SawtoothWave(frequency, 1/40, amplitude))
            waves.append(Rest(1 / 40))
        Note.__init__(self, waves)

    # def __add__(self, other: Note) -> Note:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def get_waves(self) -> typing.List[ANYWAVE]:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def get_duration(self) -> float:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body
    #
    # def play(self) -> numpy.ndarray:
    #     """ TODO: write a docstring for this method """
    #     pass  # TODO: finish this method body

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
    # python_ta.check_all(config={'extra-imports': ['helpers',
    #                                               'typing',
    #                                               'csv',
    #                                               'numpy'],
    #                             'disable': ['E9997']})


    # test step 4
    # waves = []
    # for i in range(1, 6):
    #     waves.append(SimpleWave(440 * i, 1, 1))
    # complex1 = ComplexWave(waves[:2])
    # complex2 = ComplexWave(waves[2:])
    # my_note = Note([complex1, complex2])
    # play_sound(my_note)

    #debug
    # sawtooth = SawtoothWave(440, 1, 1)
    # play_sound(sawtooth)

    # test step 5
    # sawtooth = SawtoothWave(440, 1, 1)
    # square = SquareWave(440, 1, 1)
    # rest = Rest(1)
    # play_sound(sawtooth)
    # play_sound(rest)
    # play_sound(square)

    #make sawtooth list
    # waves = []
    # for k in range(1, 11):
    #     waves.append(SimpleWave(k * 440, 1 / k, 1))
    # for wave in waves:
    #     print(wave.freq)

    #test step 6 stutternote
    # my_note = StutterNote(440, 1, 1)
    # play_sound(my_note)
