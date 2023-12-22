const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        const Cert = [310001, 310001];
        const ET = 20240131;
        const npid = 30001; 

        let result = await deployedBAKASUAV.UpdateCert(Cert, ET, npid);
        console.log("UpdateCert for UAV2:");     
        console.log("pid:",npid);
        console.log("Cert:",Cert);
        console.log("Expiry Time:",ET);
        console.log("UpdateCert for UAV2 Successfully");

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};