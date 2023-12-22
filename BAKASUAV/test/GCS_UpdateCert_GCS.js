const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        const Cert = [110001, 110001]; 
        const ET = 20240131; 
        const npid = 10001; 

        
        let result = await deployedBAKASUAV.UpdateCert(Cert, ET, npid);
        console.log("UpdateCert for GCS:");
        console.log("pid:",npid);
        console.log("Cert:",Cert);
        console.log("Expiry Time:",ET);
        console.log("UpdateCert for GCS Successfully");

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};