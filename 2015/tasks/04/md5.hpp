#ifndef MY_MD5
#define MY_MD5
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <openssl/md5.h>
namespace MyMd5 {
    std::string do_md5(std::string const& string_to_hash) {
	const unsigned char *d = reinterpret_cast<const unsigned char *>(string_to_hash.data());
	unsigned char md[MD5_DIGEST_LENGTH];
	MD5(d, static_cast<unsigned long>(string_to_hash.size()), md);
	
	std::stringstream ss;
	ss<<std::hex<<std::setfill('0');
	for (auto c : md) {
	    ss << std::setw(2)<< static_cast<int>(c);
	};
	return ss.str();
    };
};
#endif
