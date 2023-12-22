const BAKASUAV = artifacts.require("BAKASUAV");

module.exports = async function(callback) {
    try {
        const deployedBAKASUAV = await BAKASUAV.deployed();

        // GCS
        const GCSAddress = "0x3Dc856c56aC62FA1Bd4c5b560B8740AffB4f566A"; 

        // PID
        const pid = process.argv[4];

        let result = await deployedBAKASUAV.QueryCert(pid, {from: GCSAddress});
        console.log("pid:", pid);
        console.log("Cert: ", result.Cert);
        console.log("ET: ", result.ET);

    } catch (error) {
        console.error("Error in script:", error);
    }

    callback();
};
