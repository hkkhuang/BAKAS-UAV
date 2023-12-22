const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        const specificAccount = "0xffb0A93747a34f0bBA3A7c940E3F6d91FdE706D5";

        // "0xffb0A93747a34f0bBA3A7c940E3F6d91FdE706D5"; // UAV1
		// "0x543C1B8EEf6A9ad69cfab220C097425C1b38ACf9"  //UAV2

        const pid = process.argv[4];

        let result = await deployedBAKASUAV.QueryCred(pid, {from: specificAccount});
        console.log("Query Credential for UAV:");
        console.log("pid: ", pid);
        console.log("Cred: ", result.Cred);
        console.log("ET: ", result.ET);

    } catch (error) {
        console.error("Error in script:", error);
        
    }

    callback();
};