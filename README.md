# Dreambox Neuron

## Synopsis

Enigma2 Remote Controll Neuron 

## Installation
```bash
kalliope install --git-url https://github.com/xheen908/dreambox_neuron.git
```

## Options

| parameter        | required | default                       | choices                           | comments                     |
|------------------|----------|-------------------------------|-----------------------------------|------------------------------|
| dream_ip         | yes      | 192.168.1.2                   |                                   |                              |
| dream_port       | no       | 80                            |                                   |                              |
| dream_user       | no       | root                          |                                   |                              |
| dream_pass       | no       |                               |                                   |                              |

## Return Values

Only necessary when the neuron use a template to say something

| name      | description                        | type       | sample                    |
|-----------|------------------------------------|------------|---------------------------|
| value_key | dictionary containing all the data | dictionary | {"name":"me", "email": 2} |
| value_key | list of value                      | list       | ["val1", "val2", "val3"]  |
| value_key | string value                       | string     | "2"                       |
|

## Synapses example

Description of what the synapse will do
```yml
 - name: "zapto"
   signals:
     - order: "zap to {{ channel }}"
   neurons:      
     - dreambox:
        zap: "{{ channel }}"
    
 - name: "standby"
   signals:
     - order: "switch tv off"
   neurons:      
     - dreambox:
        standby: "standby"

 - name: "mute"
   signals:
     - order: "switch sound on"
     - order: "switch sound off"
   neurons:      
     - dreambox:
        mute: "mute"
 
 - name: "volup"
   signals:
     - order: "tv volume up"
   neurons:      
     - dreambox:
        volup: "volup"

 - name: "voldown"
   signals:
     - order: "tv volume down"
   neurons:      
     - dreambox:
        volup: "volup" 

 - name: "setvol"
   signals:
     - order: "set volume {{ num }}%"
   neurons:      
     - dreambox:
        setvol: "setvol"

 - name: "back"
   signals:
     - order: "back"
   neurons:      
     - dreambox:
        back: "back"

 - name: "timeshift"
   signals:
     - order: "timeshift"
   neurons:      
     - dreambox:
        timeshift: "timeshift"

```


## Templates example 

Description of the template
```
This is a var {{ var }} 
{% for item in items %}
 This is the  {{ item }}  
{% endfor %}
```

## Notes

> **Note:** This is an important note concerning the neuron

## Licence

Here define or link the licence you want to use.
