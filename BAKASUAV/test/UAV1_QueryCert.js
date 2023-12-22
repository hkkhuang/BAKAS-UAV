const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // UAV1
        const UAVAddress = "0xffb0A93747a34f0bBA3A7c940E3F6d91FdE706D5"; 

        //  PID
        const pid = process.argv[4];

        let result = await deployedBAKASUAV.QueryCert(pid, {from: UAVAddress});
        console.log("pid:", pid);
        console.log("Cert: ", result.Cert);
        console.log("ET: ", result.ET);

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};
