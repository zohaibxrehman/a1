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
    A sine wave.

    === Private Attributes ===
    _frequency: frequency of the simple wave
    _duration: duration of the simple wave
    _amplitude: amplitude of the simple wave
    """
    _frequency: int
    _duration: float
    _amplitude: float

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the simple wave.
        Precondition: 0 <= amplitude <= 1
        """
        self._frequency = frequency
        self._duration = duration
        self._amplitude = amplitude

    def __eq__(self, other: SimpleWave) -> bool:
        """Return true if this simple wave and other simple wave are equal.
        """
        return (self._frequency == other._frequency and
                self.get_duration() == other.get_duration() and
                self._amplitude == other._amplitude)

    def __ne__(self, other: SimpleWave) -> bool:
        """Return true if this simple wave and other simple wave are not
        equal.
        """
        return not (self._frequency == other._frequency and
                    self.get_duration() == other.get_duration() and
                    self._amplitude == other._amplitude)

    def __add__(self,
                other: ANYWAVE) -> ComplexWave:
        """Return a complex wave produced by the addition of this simple wave
        and <other> simple wave."""
        return ComplexWave([self, other])

    def get_duration(self) -> float:
        """Return duration of a simple wave instance in seconds."""
        return self._duration

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents a simple sine wave based on the
         frequency and duration of the simple wave.
         """
        return make_sine_wave_array(self._frequency,
                                    self.get_duration()) * self._amplitude


class ComplexWave:
    """
    A complex wave comprising of simple waves.

    === Private Attribute ===
    _waves: list of simple waves that build this complex wave
    """
    _waves: typing.List[SimpleWave]

    def __init__(self, waves: typing.List[SimpleWave]) -> None:
        """Initialises the complex wave.
        Precondition: duration of each simple wave should be
        equal.
        """
        self._waves = waves

    def __add__(self,
                other: ANYWAVE) -> ComplexWave:
        """Return the sum of a complex wave and another wave.
        """
        if isinstance(other, SimpleWave):
            return ComplexWave(self.get_waves() + [other])
        else:
            return ComplexWave(self.get_waves() + other.get_waves())

    def complexity(self) -> int:
        """Return the complexity of the complex wave.
        """
        return len(self.get_waves())

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents a wave based on the additive
        synthesis of its simple waves.
        """
        if len(self.get_waves()) != 0:
            arr = self.get_waves()[0].play()
            for wave in self.get_waves()[1:]:
                size = arr.size
                wave_arr = wave.play()
                if size > wave_arr.size:
                    wave_arr.resize(arr.shape)
                elif size < wave_arr.size:
                    arr.resize(wave_arr.shape)
                arr = arr + wave_arr
            if arr.size == 0:
                return arr
            else:
                abs_max = abs(arr.max()) if abs(arr.max()) > abs(arr.min()) \
                    else abs(arr.min())
                if abs_max > 1:
                    return arr / abs_max
                else:
                    return arr
        else:
            return numpy.array([])

    def get_waves(self) -> typing.List[SimpleWave]:
        """Return a list of SimpleWave instances that can be added together
        to represent a ComplexWave instance."""
        return self._waves

    def get_duration(self) -> float:
        """Return the duration of the complex wave. This duration is the maximum
         duration of its simple waves"""
        lst = []
        for wave in self.get_waves():
            lst.append(wave.get_duration())
        return max(lst)


class Note:
    """
    A note is a series of different waves (complex or simple) played in order,
    one after the other.

    === Public Attribute ===
    amplitude: amplitude of the Note

    === Private Attribute ===
    _waves: list of simple/complex waves that this note comprises of
    """
    amplitude: float
    _waves: typing.List[ANYWAVE]

    def __init__(self, waves: typing.List[ANYWAVE]) -> None:
        """Initialise the Note.
        """
        self.amplitude = 1
        self._waves = waves

    def __add__(self, other: Note) -> Note:
        """Return the sum of this note and the other note.
        The amplitude of the result will be the greatest amplitude of the two
        combined Note instances.
        """
        beat = Note(self.get_waves() + other.get_waves())
        beat.amplitude = max(self.amplitude, other.amplitude)
        return beat

    def get_waves(self) -> typing.List[ANYWAVE]:
        """Return a list of waves (ComplexWave or SimpleWave instances) that
        represent the waves that, if played in order with no pauses in between,
        would sound exactly like playing the Note instance, that is, the
        components of this Note.
        """
        return self._waves

    def get_duration(self) -> float:
        """Return the duration of this note."""
        dur = 0
        for wave in self.get_waves():
            dur = dur + wave.get_duration()
        return dur

    def play(self) -> numpy.ndarray:
        """Return a numpy array which represents the note.
        """
        if len(self.get_waves()) != 0:
            arr = self.get_waves()[0].play()
            for wave in self.get_waves()[1:]:
                arr = numpy.append(arr, wave.play())
            if arr.size == 0:
                return arr
            else:
                abs_max = abs(arr.max()) if abs(arr.max()) > abs(arr.min()) \
                    else abs(arr.min())
                if abs_max != 0:
                    return arr * (self.amplitude / abs_max)
                else:
                    return arr
        else:
            return numpy.array([])


class SawtoothWave(ComplexWave):
    """
    A sawtooth wave is a complex wave composed of an infinite number of
    components which follow a distinct pattern.

    === Private Attribute ===
    _waves: list of simple waves that build this sawtooth wave
    """
    _waves: typing.List[SimpleWave]

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the sawtooth wave.
        Precondition: 0 <= amplitude <= 1
        """
        waves = []
        for k in range(1, 11):
            waves.append(SimpleWave(k * frequency, duration,
                                    amplitude / k))
        ComplexWave.__init__(self, waves)


class SquareWave(ComplexWave):
    """
    A square wave is similar to a sawtooth wave but the kth component of a
    square wave has a frequency equal to (2k-1)F and an amplitude
    equal to A/(2k-1).

    === Private Attribute ===
    _waves: list of simple waves that build this square wave
    """
    _waves: typing.List[SimpleWave]

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the square wave.
        Precondition: 0 <= amplitude <= 1
        """
        waves = []
        for k in range(1, 11):
            waves.append(SimpleWave((2 * k - 1) * frequency, duration,
                                    amplitude / (2 * k - 1)))
        ComplexWave.__init__(self, waves)


class Rest(ComplexWave):
    """
    A rest describing a period of silence where no sound is played.

    === Private Attribute ===
    _waves: list of simple waves that build this rest
    """
    _waves: typing.List[SimpleWave]

    def __init__(self, duration: float) -> None:
        """Initialise the rest"""
        ComplexWave.__init__(self, [SimpleWave(0, duration, 0)])


class StutterNote(Note):
    """
    A stutter note is a note that alternates between playing a sawtooth wave
    for a fixed period of time followed by silence for the same period of time.

    === Public Attribute ===
    amplitude: amplitude of the Note

    === Private Attribute ===
    _waves: list of simple/complex waves that this note comprises of
    """
    amplitude: float
    _waves: list

    def __init__(self, frequency: int,
                 duration: float, amplitude: float) -> None:
        """Initialises the stutter note.
        The number of waves created are rounded down if durations produces a
        decimal.
        Precondition: 0 <= amplitude <= 1
        """
        waves = []
        last_created = ''
        for i in range(int(duration / (1 / 40))):
            if i % 2 == 0:
                waves.append(SawtoothWave(frequency, 1 / 40, amplitude))
                last_created = 'sawtooth'
            else:
                waves.append(Rest(1 / 40))
                last_created = 'rest'

        remainder = round(duration - int(duration / (1 / 40)) * (1/40), 4)
        if last_created == 'rest' and remainder != 0.0:
            waves.append(SawtoothWave(frequency, remainder, amplitude))
        elif last_created == 'sawtooth' and remainder != 0.0:
            waves.append(Rest(remainder))
        Note.__init__(self, waves)
        self.amplitude = amplitude


class Instrument:
    """
    Superclass for the instruments.

    === Private Attribute ===
    _note: the currently stored note
    """
    _note: Note

    def __init__(self) -> None:
        """Initialises the instrument.
        """
        self._note = Note([])

    def get_duration(self) -> float:
        """Return the duration of the baliset.
        """
        return self._note.get_duration()

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
        return self._note.play()


class Baliset(Instrument):
    """
    An instrument that has a fundamental frequency of 196 Hz and
    plays a sawtooth wave

    === Private Attribute ===
    _note: the currently stored note
    """
    _note: Note

    def __init__(self) -> None:
        """Initialises the baliset.
        """
        Instrument.__init__(self)

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object
        """
        waves = []
        for info in note_info:
            if info[0] != 'rest':
                ratio_lst = info[0].strip().split(':')
                ratio = float(ratio_lst[0]) / float(ratio_lst[1])
                waves.append(SawtoothWave(int(196 * ratio), info[2], info[1]))
            else:
                waves.append(Rest(info[2]))
        self._note = Note(waves)


class Holophonor(Instrument):
    """
    An instrument that has a fundamental frequency of 65 Hz and
    plays a stutter note.

    === Private Attribute ===
    _note: the currently stored note
    """
    _note: Note

    def __init__(self) -> None:
        """Initialises the holophonor.
        """
        Instrument.__init__(self)

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object.
        """
        waves = []
        if len(note_info) != 0:
            ratio_lst = note_info[0][0].strip().split(':')
            if ratio_lst[0] == 'rest':
                waves.append(Rest(note_info[0][2]))
            else:
                ratio = float(ratio_lst[0]) / float(ratio_lst[1])
                waves.append(StutterNote(int(ratio * 65), note_info[0][2],
                                         note_info[0][1]))

            for info in note_info[1:]:
                ratio_lst = info[0].strip().split(':')
                if ratio_lst[0] != 'rest':
                    ratio = float(ratio_lst[0]) / float(ratio_lst[1])
                    wave = StutterNote(int(ratio * 65), info[2], info[1])
                    waves.append(wave)
                else:
                    wave = Rest(info[2])
                    waves.append(wave)
            self._note = Note(waves)


class Gaffophone(Instrument):
    """
    An instrument that has a fundamental frequency of 131 Hz and
    plays two square waves at the same time. The first wave’s frequency is
    calculated normally but the second wave has a frequency that is 3/2 times
    the first wave’s frequency.

    === Private Attribute ===
    note: the currently stored note
    """
    _note: Note

    def __init__(self) -> None:
        """Initialises the gaffophone.
        """
        Instrument.__init__(self)

    def next_notes(self,
                   note_info: typing.List[typing.Tuple[str, float, float]]
                   ) -> None:
        """Calculate the  next series of Notes, SimpleWaves and/or ComplexWaves
        to play based on the arguments (see docstring) and store it somewhere
        as a Note object.
        """
        waves = []
        for info in note_info:
            if info[0] != 'rest':
                ratio_lst = info[0].strip().split(':')
                ratio = float(ratio_lst[0]) / float(ratio_lst[1])
                waves.append(
                    SquareWave(int(131 * ratio), info[2], info[1]) + SquareWave(
                        int(131 * 3 / 2 * ratio), info[2], info[1]))
            else:
                waves.append(Rest(info[2]))
        self._note = Note(waves)


def play_song(song_file: str, beat: float) -> None:
    """
    Plays the song file <song_file> played at a beat of <beat>.
    """
    instrument_dict = _play_song_helper_1(song_file)
    argument_dict = _play_song_helper_2(instrument_dict, beat)
    seconds = max(len(argument_dict['Baliset']),
                  len(argument_dict['Holophonor']),
                  len(argument_dict['Gaffophone']))

    h = Holophonor()
    bal = Baliset()
    g = Gaffophone()
    for second in range(seconds):
        play_list = []
        if second < len(argument_dict['Baliset']):
            bal.next_notes(argument_dict['Baliset'][second])
            play_list.append(bal)
        if second < len(argument_dict['Holophonor']):
            h.next_notes(argument_dict['Holophonor'][second])
            play_list.append(h)
        if second < len(argument_dict['Gaffophone']):
            g.next_notes(argument_dict['Gaffophone'][second])
            play_list.append(g)
        play_sounds(play_list)


def _play_song_helper_1(song_file: str) -> dict:
    """Helper function for play_song.
    """
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


def _play_song_helper_2(instruments: dict, beat: float) -> dict:
    """
    Another helper function for play_song.
    """
    play_dict = {}
    for instrument in instruments:
        _play_song_helper_2_instrument(play_dict, instrument, instruments, beat)
    return play_dict


def _play_song_helper_2_instrument(play_dict: dict, instrument: str,
                                   instruments: dict, beat: float) -> None:
    """
     Helper function for _play_song_helper_2 for one instrument.
    """
    play_dict[instrument] = []
    lst = []
    remain = 0
    val = 0
    i = 0
    while i < len(instruments[instrument]) and \
            len(instruments[instrument][i]) != 0:
        note = instruments[instrument][i]
        argument_list = note.strip().split(':')
        amp = 1
        if argument_list[0] == 'rest':
            phrase = 'rest'
            sample_duration = float(argument_list[1]) * beat
        else:
            phrase = str(argument_list[0]) + ':' + str(argument_list[1])
            sample_duration = float(argument_list[3]) * beat
            amp = float(argument_list[2])
        remain += sample_duration
        dur = round(sample_duration, 2)
        if remain > 1:
            val = round(remain - 1, 2)
            remain = 1
            dur = round(sample_duration - val, 2)
        if remain == 1:
            if dur != 0:
                lst.append((phrase, amp, dur))
            play_dict[instrument].append(lst)
            remain += val
            lst = []
        elif remain < 1 and dur != 0:
            lst.append((phrase, amp, dur))
        if remain >= 1:
            remain -= 1
            while remain >= 1:
                play_dict[instrument].append([(phrase, amp, 1)])
                remain -= 1
            if remain != 0:
                lst.append((phrase, amp, round(remain, 2)))
            val = 0
        if (instruments[instrument].index(note) == len(
                instruments[instrument]) - 1) and remain != 0:
            lst.append(('rest', 1, round(1 - remain, 2)))
            play_dict[instrument].append(lst)
        i = i + 1


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
    # python_ta.check_all(
    #     config={'extra-imports': ['helpers', 'typing', 'csv', 'numpy'],
    #             'disable': ['E9997', 'E9998', 'W0611']})
    # play_song('spanish_violin.csv', 0.2)
