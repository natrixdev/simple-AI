# Simple AI using Python<br/><br/>
This is a simple IA written in Python that can answer basic questions about the weather and USB connections. The AI is capable of responding to the following types of questions:

- "What's the weather like today?"
- "Will it rain later?"
- "How do I connect a USB to my computer?"
- "My computer isn't recognizing the USB, what do I do?"

# How it works<br/><br/>
The AI is designed to respond to user input based on the presence of certain keywords. If the user input contains the word "weather", the IA will respond with a random weather-related response from a predefined list. If the user input contains the word "usb", the AI will respond with a random USB-related response from another predefined list. If the user input does not contain any of these keywords, the AI will respond with a random greeting from yet another predefined list.

# How to use<br/><br/>
To use the AI, simply instantiate the SimpleIA class and call the respond method with a string representing the user's question. The respond method will return a string containing the IA's response. Here's an example:

```PYTHON
from ia import SimpleIA

ia = SimpleIA()
response = ia.respond("What's the weather like today?")
print(response) # "Expect some rain later"
```

**Support:** <br/>
| Star                                     | Fork                                     |
| ---------------------------------------- | ---------------------------------------- |
| ![Star](https://i.imgur.com/41nhvJ1.png) | ![Fork](https://i.imgur.com/MOtHDPV.png) |

