const parseData = (data, observationList) => {

    const keyMap = {
        'temperature': 't2m',
        'humidity': 'Humidity',
        'wind': 'WindSpeedMS', 
    };

    const respData = {};

    observationList.forEach(element => {
        const obsData = data[keyMap[element]];
        respData[element] = obsData[obsData.length -1][1];
        
    });
}