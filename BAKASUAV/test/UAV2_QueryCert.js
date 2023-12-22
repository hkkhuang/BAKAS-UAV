const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // UAV1
        const UAVAddress = "0x543C1B8EEf6A9ad69cfab220C097425C1b38ACf9"; 

        // PID
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