# Definition
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class

# behavior design pattern

# Ugly code, not using state pattern
- Code should be changed every time when new states arise, or behavior is changed.
- Code will be bigger as a new requirements would be needed.

```
class Document is
    field state: string
    // ...
    method publish() is
        switch (state)
            "draft":
                state = "moderation"
                break
            "moderation":
                if (currentUser.role == "admin")
                    state = "published"
                break
            "published":
                // Do nothing.
                break
    // ...
```
# Solution
![image](https://github.com/devhanee1/designPattern/assets/37257706/b55d2c78-9cc1-42c4-8c30-08adc4bb3d06)
![image](https://github.com/devhanee1/designPattern/assets/37257706/6fe4da7d-61ba-4977-a54d-fe31b6f947b6)

```
class AudioPlayer is
  field state: State
  field Ui, volume, ..

  constructor AudioPlayer() is
    this.state = new ReadyState(this)

  method changeState(state: State) is
    this.state = state

  method clickLock() is
    state.clickLock()
  method clickPlay() is
    state.clickPlay()

  // A state may call some service method on the context
  method startPlayback() is ...
  method stopPlayerback() is ...

abstract class State is
  protected field player: AudioPlayer

  constuctor State(player) is
    this.player = player

  abstract method clickLock()
  abstract method clickPlay()

class LockedState extends State is
  method clickLock() is
    if(player.playing)
      player.changeState(new PlayerState(player))
    else
      player.changeState(new ReadyState(player))

  method clickPlayer() is
    // Lock , do nothing

class ReadyState extends State is
  method clickLock() is
    player.changeState(new LockedState(player))

  method clickPlay() is
    player.startPlayback()
    player.changeState(new PlayerState(player))
```

<hr>

- Reference
  - https://refactoring.guru/design-patterns/state
