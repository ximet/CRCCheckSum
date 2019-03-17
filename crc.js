const START_VALUE = 0xFFFFFFFF;

const stringToArrayBytes = (string) => {
    const bytes = new Uint32Array(string.length);

    for (let i = 0; i < string.length; i++) {
        bytes[i] = string.charCodeAt(i);
    }

    return bytes;
}

const generateCRCTable = () => {
    const COUNT_VALUES = 256;
    const CRC_TABLE = new Uint32Array(COUNT_VALUES);

    for (let i = 0; i < COUNT_VALUES; i++) {
        let value = i;
        let count_bit = 8;
        while (count_bit--) {
            value = (value >>> 1) ^ ((value & 1) ? 0xEDB88320 : 0);
        }
        CRC_TABLE[i] = value;
    }

    return CRC_TABLE;
};



console.log(stringToArrayBytes('test'));

const crc = (data) => {
    
}