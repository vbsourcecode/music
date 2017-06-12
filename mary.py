import midi

MARY_MIDI = midi.Pattern(tracks=[[midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),
  midi.KeySignatureEvent(tick=0, data=[0, 0]),
  midi.EndOfTrackEvent(tick=1, data=[])],
 [midi.ControlChangeEvent(tick=0, channel=0, data=[91, 58]),
  midi.ControlChangeEvent(tick=0, channel=0, data=[10, 69]),
  midi.ControlChangeEvent(tick=0, channel=0, data=[0, 0]),
  midi.ControlChangeEvent(tick=0, channel=0, data=[32, 0]),
  midi.ProgramChangeEvent(tick=0, channel=0, data=[24]),
  midi.NoteOnEvent(tick=0, channel=0, data=[64, 72]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 70]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 72]),
  midi.NoteOnEvent(tick=231, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[60, 71]),
  midi.NoteOnEvent(tick=231, channel=0, data=[60, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 79]),
  midi.NoteOnEvent(tick=206, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 85]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 79]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 78]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 74]),
  midi.NoteOnEvent(tick=462, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=50, channel=0, data=[62, 75]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 77]),
  midi.NoteOnEvent(tick=231, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 77]),
  midi.NoteOnEvent(tick=231, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 75]),
  midi.NoteOnEvent(tick=462, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=0, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=50, channel=0, data=[64, 82]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 79]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[67, 84]),
  midi.NoteOnEvent(tick=231, channel=0, data=[67, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[67, 75]),
  midi.NoteOnEvent(tick=462, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=0, channel=0, data=[67, 0]),
  midi.NoteOnEvent(tick=50, channel=0, data=[64, 73]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 78]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 69]),
  midi.NoteOnEvent(tick=231, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[60, 71]),
  midi.NoteOnEvent(tick=231, channel=0, data=[60, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 80]),
  midi.NoteOnEvent(tick=206, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 84]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 79]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 76]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 74]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 77]),
  midi.NoteOnEvent(tick=206, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 75]),
  midi.NoteOnEvent(tick=0, channel=0, data=[55, 78]),
  midi.NoteOnEvent(tick=231, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 74]),
  midi.NoteOnEvent(tick=231, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[64, 81]),
  midi.NoteOnEvent(tick=231, channel=0, data=[64, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 70]),
  midi.NoteOnEvent(tick=206, channel=0, data=[55, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[62, 0]),
  midi.NoteOnEvent(tick=25, channel=0, data=[60, 73]),
  midi.NoteOnEvent(tick=0, channel=0, data=[52, 72]),
  midi.NoteOnEvent(tick=974, channel=0, data=[60, 0]),
  midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
  midi.EndOfTrackEvent(tick=1, data=[])]])

midi.write_midifile("mary33.mid", MARY_MIDI)