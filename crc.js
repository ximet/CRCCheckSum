const START_VALUE = 0xFFFFFFFF;

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



console.log(generateCRCTable());

const crc = (data) => {
    
}