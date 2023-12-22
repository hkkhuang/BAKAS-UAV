// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BAKASUAV {
    address public GCS; 
    uint256 public round;

    struct Credential {  
        uint160 PID;
        uint256[2] Cred; // Cert  Cred_p, Cred_n
        uint32 ET;       // unit32 ET
    }

    struct Certificate {
        uint160 PID;      
        uint256[2] Cert;  // Cert  Cert_p, Cert_n
        uint32 ET;        // unit32 ET
    }

    mapping(uint256 => Credential) public CredentialT;    
    mapping(uint256 => Certificate) public CertificateT;  
    mapping(address => bool) public registeredUAVs;

    event _UpdateCert(address indexed requester); 
    event _UpdateCred(address indexed requester); 
    event _QueryCert(address indexed requester);  
    event _QueryCred(address indexed requester);  


    constructor() {
        GCS = msg.sender;
        round = 0;
    }

    function registerUAV(address _UAV) public {
        require(msg.sender == GCS, "Only GCS can register UAV.");
        registeredUAVs[_UAV] = true;
    }

    function UpdateCert(uint256[2] memory Cert, uint32 ET, uint160 npid) public returns (address addr){ 
        require(msg.sender == GCS, "Only GCS can update its public key.");
        
        CertificateT[round].PID=npid;
        CertificateT[round].Cert=Cert;
        CertificateT[round].ET = ET;
        round++;
        emit _UpdateCert(msg.sender); 
        return msg.sender;
    }

    function UpdateCred(uint256[2] memory Cred, uint32 ET, uint160 npid) public returns (address addr){ 
        require(registeredUAVs[msg.sender], "Only registered UAV can update its credentials.");
        
        CredentialT[round].PID=npid;
        CredentialT[round].Cred=Cred;
        CredentialT[round].ET = ET;
        round++; 
        emit _UpdateCred(msg.sender);
        return msg.sender;
    }

    function QueryCert(uint256 pid) public view returns (uint256[2] memory Cert, uint32 ET, bool found) {
        // _QueryCert(msg.sender);
        for (uint256 i = 0; i < round; i++) {
            if (CertificateT[i].PID == pid) {
                return (CertificateT[i].Cert, CertificateT[i].ET, true);
            }
        }
        
        // return (CertificateT[pid].Cert, CertificateT[pid].ET);
    }

    function QueryCred(uint256 pid) public view returns (uint256[2] memory Cred, uint32 ET, bool found) {
        // _QueryCred(msg.sender); 
        for (uint256 i = 0; i < round; i++) {
            if (CredentialT[i].PID == pid) {
                return (CredentialT[i].Cred, CredentialT[i].ET, true);
            }
        }
        return (Cred, ET, false);
    }
}
