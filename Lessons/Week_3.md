# Blockchain 11/09/23

## Cryptography and digital signature

### Foundation of blockchain

Blockchain is a brilliant integration of the concepts from cryptography (valid transaction and block), game theory (consensus and chain validity in distributed ledger (double spend attack)) and computer science engineering (data structures and P2P network communication).

Roles ?

The traditional approach was that there would be a centralized entity that would maintain just one transaction/ modification history.

A centralized system:

- has to be trusted
- Cost and time
- Centralization of power.

### Cryptography

Cryptography is the most important component of blockchain.

It is the science of keeping things confidential using encryption techniques. However, confidentiality is not the only objective.

- Cipher is a system of writing that prevents most people form understanding the message. ( Greek Scytable 7th century)

This cryptographic technique served two main purposes:

- protecting the integrity of messages
- maintenaing secrecy

To maintain the secret we need :

- Confidentiality, only the intended or authorized recipient can understand the message.
- It can also be referred to as privacy and secrecy.

- Data Integrity, data cannot be forged or modified by an adversary intentionally or by unintended/accidental errors.Though data integrity cannot prevent the alteration of data, it an provide a means of detecting whether the data was modified.
- Authentication, the authenticity  of the sender is assured and verifiable by the receiver.
- Non-repudiation, the sender after sending a message, cannot deny later that they sent the message.
- This means that an entity (a person or a system) cannot refuse the ownership of a previous commitment or an action.

### Summarize

Any information in the form of a text message, numeric data, or a computer program can be called plaintext.

The idea is to encrypt the plaintext using an encryption algorithm and a key that produces the ciphertext.
 ...

### Types of cryptography

There are two kinds of cryptography:

- symmetric key (private key) cryptography : encrypt and decrypt

- Asymmetric key (public key) cryptography.

Limitations in symmetric key crypto :
The key must be shared by the sender and the receiver before any communication. It requires a secured key establishment mechanism in place.

The sender and receiver must trust each other, as they use the same

Asymmetric

public key : encrypt or verify the signatures  (know and accessible to everyone)

private key : decryt and create signatures. (are extemely privagte to indivuals)

the public key should be kept in a public repository accessible to everyone and the private key should have to access this one.
