const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        const pid = process.argv[4]; 

        //GCS
        const specificAccount = "0x3Dc856c56aC62FA1Bd4c5b560B8740AffB4f566A";

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