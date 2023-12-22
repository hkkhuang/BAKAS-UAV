const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        const Cert = [210001, 210001];
        const ET = 20240131;
        const npid = 20001;

        let result = await deployedBAKASUAV.UpdateCert(Cert, ET, npid);
        console.log("UpdateCert for UAV1:");     
        console.log("pid:",npid);
        console.log("Cert:",Cert);
        console.log("Expiry Time:",ET);
        console.log("UpdateCert for UAV1 Successfully");

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};