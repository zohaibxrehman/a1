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
    freq: int # FIXME WHAT IS TYPE? INT OR FLOAT
    duration: float
    amp: float

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the simple wave.
        Precondition: 0 <= amplitude <= 1
        """
        self.freq = frequency
        self.duration = duration
        self.amp = amplitude

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

    def get_duration(self) -> float:
        """Return duration of a SimpleWave instance in seconds."""
        return self.duration

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents a simple sine wave based on the
         frequency and duration of the simple wave.
         """
        return make_sine_wave_array(self.freq, self.duration) * self.amp


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
        if len(self.waves) != 0 and self.play_helper():
            arr = self.waves[0].play()
            for wave in self.waves[1:]:
                arr = arr + wave.play()
                #  numpy.add?
            abs_max = abs(arr.max()) if abs(arr.max()) > abs(arr.min()) \
                else abs(arr.min())
            if abs_max != 0:
                return arr / abs_max
            else:
                return arr

    def play_helper(self) -> bool:
        """
        Helper method for play(). Return true when all the waves have the
        same duration.

        Precondition: len(self.waves()) > 0
        """
        length = self.waves[0].duration
        for arr in self.waves:
            if arr.duration != length:
                return False
        return True

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
        """Return a numpy array which represents the note."""
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
        waves = []
        for k in range(1, 11):
            waves.append(SimpleWave(k * frequency, duration,
                                    amplitude / k))
        ComplexWave.__init__(self, waves)

    # def __add__(self,
    #             other: ANYWAVE) -> ComplexWave:
    #     """ """

    # def complexity(self) -> int:
    #     """ """
    #     return len()

    # def play(self) -> numpy.ndarray:
    #     """ """
    #     pass

    # def get_waves(self) -> typing.List[SimpleWave]:
    #     """  """
    #     pass

    # def get_duration(self) -> float:
    #     """ """
    #     pass

    # def simplify(self) -> None:
    #     """
    #         REMEMBER: this is not a required part of the assignment
    #     """
    #     pass


class SquareWave(ComplexWave):
    """

    === Attributes ===
    waves: list of simple waves that build this complex wave
    """
    waves: list

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the square wave.
        """
        waves = []
        for k in range(1, 11):
            waves.append(SimpleWave((2 * k - 1) * frequency, duration,
                                    amplitude / (2 * k - 1)))
        ComplexWave.__init__(self, waves)

    # def __add__(self,
    #             other: ANYWAVE) -> ComplexWave:
    #     """ """
    #     pass
    #
    # def complexity(self) -> int:
    #     """ """
    #     pass
    #
    # def play(self) -> numpy.ndarray:
    #     """ """
    #     pass
    #
    # def get_waves(self) -> typing.List[SimpleWave]:
    #     """ """
    #     pass
    #
    # def get_duration(self) -> float:
    #     """ """
    #     pass
    #
    # def simplify(self) -> None:
    #     """
    #         REMEMBER: this is not a required part of the assignment
    #     """
    #     pass


class Rest(ComplexWave):
    """

    """
    waves: list

    def __init__(self, duration: float) -> None:
        """Initialise the rest"""
        ComplexWave.__init__(self, [SimpleWave(0, duration, 0)])

    # def __add__(self,
    #             other: ANYWAVE) -> ComplexWave:
    #     """ """
    #     pass
    #
    # def complexity(self) -> int:
    #     """ """
    #     pass
    #
    # def play(self) -> numpy.ndarray:
    #     """ """
    #     pass
    #
    # def get_waves(self) -> typing.List[SimpleWave]:
    #     """ """
    #     pass  #
    #
    # def get_duration(self) -> float:
    #     """ """
    #     pass
    #
    # def simplify(self) -> None:
    #     """
    #         REMEMBER: this is not a required part of the assignment
    #     """
    #     pass


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
        The number of waves created are rounded down if durations produces a
        decimal.
        """
        waves = []
        for i in range(int(20 * duration)):
            # FIXME int or ceil? int(floor) makes sense
            waves.append(SawtoothWave(frequency, 1/40, amplitude))
            waves.append(Rest(1 / 40))
        Note.__init__(self, waves)

    # def __add__(self, other: Note) -> Note:
    #     """ """
    #     pass  #
    #
    # def get_waves(self) -> typing.List[ANYWAVE]:
    #     """ """
    #     pass  #
    #
    # def get_duration(self) -> float:
    #     """ """
    #     pass  #
    #
    # def play(self) -> numpy.ndarray:
    #     """ ""
    #     pass  #


class Instrument:
    """
    Superclass for the instruments.

    === Attributes ===
    note: the currently stored note
    """
    note: Note

    def __init__(self) -> None:
        """Initialises the baliset
        """
        self.note = Note([]) # FIXME init doesn't seem perfect

    def get_duration(self) -> float:
        """Return the duration of the baliset.
        """
        return self.note.get_duration()

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object
        """
        raise NotImplementedError

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents the baliset.
        """
        return self.note.play()


class Baliset(Instrument):
    """
    === Attributes ===
    note: the currently stored note
    """
    note: Note

    def __init__(self) -> None:
        """Initialises the baliset.
        """
        Instrument.__init__(self)

    # def get_duration(self) -> float:
    #     """Return the duration of the baliset.
    #     """
    #     return self.note.get_duration()

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object
        """
        waves = []
        for info in note_info:
            ratio_lst = info[0].strip().split(':')
            ratio = float(ratio_lst[0]) / float(ratio_lst[1])
            # FIXME optimize? int?
            waves.append(SawtoothWave(int(196 * ratio), info[2], info[1]))
            # FIXME BIGTIME: FLOAT VALUE FOR FREQ?
            # FIXME !!!
            # FIXME !!!
        self.note = Note(waves)

    # def play(self) -> numpy.ndarray:
    #     """Return a numpy array which represents the baliset.
    #     """
    #     return self.note.play()


class Holophonor(Instrument):
    """
    === Attributes ===
    note: the currently stored note
    """
    note: Note

    def __init__(self) -> None:
        """Initialises the holophonor.
        """
        Instrument.__init__(self) # comeback and FIXME. stutternote

    # def get_duration(self) -> float:
    #     """  """
    #     pass  #

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object.
        """
        if len(note_info) != 0:
            ratio_lst = note_info[0][0].strip().split(':')
            ratio = float(ratio_lst[0]) / float(ratio_lst[1])
            waves = StutterNote(int(ratio * 65), note_info[0][2], note_info[0][1])
            for info in note_info[1:]:
                ratio_lst = info[0].strip().split(':')
                ratio = float(ratio_lst[0]) / float(ratio_lst[1])
                wave = StutterNote(int(ratio * 65), info[2], info[1])
                # FIXME optimize? int?
                waves = waves + wave
                # FIXME BIGTIME: FLOAT VALUE FOR FREQ?
            self.note = waves

    # def play(self) -> numpy.ndarray:
    #     """  """
    #     pass


class Gaffophone(Instrument):
    """
    === Attributes ===
    note: the currently stored note
    """
    note: Note

    def __init__(self) -> None:
        """Initialises the gaffophone.
        """
        Instrument.__init__(self)

    # def get_duration(self) -> float:
    #     """ """
    #     pass

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object.
        """
        waves = []
        for info in note_info:
            ratio_lst = info[0].strip().split(':')
            ratio = float(ratio_lst[0]) / float(ratio_lst[1])
            # FIXME optimize? int?
            waves.append(SquareWave(int(131 * ratio), info[2], info[1]) +
                         SquareWave(int(131 * 3/2 * ratio), info[2], info[1]))
            # FIXME BIGTIME: FLOAT VALUE FOR FREQ?
            # FIXME !!!
            # FIXME !!!
        self.note = Note(waves)
    # def play(self) -> numpy.ndarray:
    #     """ """
    #     pass


def play_song(song_file: str, beat: float) -> None:
    """ """
    instrument_dict = play_song_helper_1(song_file)
    argument_dict = play_song_helper_2(instrument_dict, beat)
    seconds = max(len(argument_dict['Baliset']),
                  len(argument_dict['Holophoner']),
                  len(argument_dict['Gaffophone']))

    for second in range(seconds):
        play_list = []
        if second < len(argument_dict['Baliset']):
            b = Baliset()
            b.next_notes(argument_dict['Baliset'][second])
            play_list.append(b)

        if second < len(argument_dict['Holophonor']):
            h = Holophonor()
            h.next_notes(argument_dict['Holophonor'][second])
            play_list.append(h)

        if second < len(argument_dict['Gaffophone']):
            g = Gaffophone()
            g.next_notes(argument_dict['Gaffophone'][second])
            play_list.append(g)

        play_sounds(play_list)


def play_song_helper_1(song_file: str) -> dict:
    """."""
    instrument_dict = {}
    with open(song_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        lines = []
        for line in reader:
            lines.append(line)
    csvfile.close()

    instrument_order = lines[0]
    note_list = lines[1:]

    for instrument in instrument_order:
        instrument_dict[instrument] = []

    for note in note_list:
        for n in range(len(note)):
            instrument_dict[instrument_order[n]].append(note[n])

    return instrument_dict


def play_song_helper_2(instruments: dict, beat: float) -> dict:
    """"""
    play_dict = {}
    for instrument in instruments:
        play_dict[instrument] = []
        lst = []
        remain = 0
        for note in instruments[instrument]:
            argument_list = note.strip().split(':')
            sample_duration = float(argument_list[2]) * beat
            amp = 1
            remain += sample_duration
            dur = sample_duration
            if remain > 1:
                val = remain - 1
                remain = 1
                dur = sample_duration - val
            if argument_list[0] == 'rest':
                phrase = 'rest'
            else:
                phrase = str(argument_list[0]) + ':' + str(argument_list[0])
                amp = float(argument_list[1])
            if remain == 1:
                lst.append((phrase, amp, dur))
                play_dict[instrument].append(lst)
                remain = val
                lst = []
            elif remain < 1:
                lst.append((phrase, amp, dur))
            if remain > 1:
                while remain < 1:
                    play_dict[instrument].append([(phrase, amp, 1)])
                    remain -= 1
                if remain != 0:
                    lst.append((phrase, amp, remain))
    return play_dict

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

    # debug
    # sawtooth = SawtoothWave(440, 1, 1)
    # play_sound(sawtooth)

    # test step 5
    # sawtooth = SawtoothWave(440, 1, 1)
    # square = SquareWave(440, 1, 1)
    # rest = Rest(1)
    # play_sound(sawtooth)
    # play_sound(rest)
    # play_sound(square)

    # make sawtooth list
    # waves = []
    # for k in range(1, 11):
    #     waves.append(SimpleWave(k * 440, 1 / k, 1))
    # for wave in waves:
    #     print(wave.freq)

    # test step 6 stutternote
    # my_note = StutterNote(440, 1, 1)
    # play_sound(my_note)

    # test step 7
    # bal = Baliset()
    # bal.next_notes([("5:4", 0.7, 1)])
    # play_sound(bal)

    # test 2 step 7
    # bal = Baliset()
    # bal.next_notes([("5:4", 0.7, 1), ("6:4", 0.7, 1), ("7:4", 0.7, 1)])
    #
    # hol = Holophonor()
    # hol.next_notes([("5:4", 0.7, 1), ("6:4", 0.7, 1)])
    #
    # bal2 = Baliset()
    # bal2.next_notes([("5:6", 0.7, 1), ("6:7", 0.7, 1), ("7:8", 0.7, 1),
    #                  ("7:9", 0.7, 1)])
    #
    # for i in range(2):
    #     play_sound(bal)
    #     play_sound(hol)
    #     play_sound(bal2)

    # test 3 step 7
    # bal = Baliset()
    # bal.next_notes([("5:4", 0.7, 1), ("6:4", 0.7, 1), ("7:4", 0.7, 1)])
    #
    # hol = Holophonor()
    # hol.next_notes([("5:4", 0.7, 1)])
    #
    # bal2 = Baliset()
    # bal2.next_notes([("5:6", 0.7, 1), ("6:7", 0.7, 1), ("7:8", 0.7, 1),
    #                  ("7:9", 0.7, 1)])
    #
    # gaf = Gaffophone()
    # gaf.next_notes([("5:4", 0.7, 1), ("6:4", 0.7, 1), ("7:4", 0.7, 1)])
    #
    # gaf2 = Gaffophone()
    # gaf2.next_notes([("5:6", 0.7, 1), ("6:7", 0.7, 1), ("7:8", 0.7, 1)])
    # #
    # for i in range(1):
    #     play_sound(bal)
    #     play_sound(hol)
    #     play_sound(gaf)
    #     play_sound(hol)
    #     play_sound(bal2)
    #     play_sound(hol)
    #     play_sound(gaf2)
    #     play_sound(hol)

    print(play_song('song.csv', 1))
