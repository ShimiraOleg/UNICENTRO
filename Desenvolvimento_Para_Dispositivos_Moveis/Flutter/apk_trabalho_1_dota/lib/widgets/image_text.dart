import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

Widget imageText(String url, String text, double space) {
  final bool isSvg = url.toLowerCase().endsWith('.svg');
  return Padding(
    padding: EdgeInsets.symmetric(vertical: space),
    child: Row(
      children: <Widget>[
        isSvg
            ? SvgPicture.network(url, width: 30, height: 30, fit: BoxFit.cover)
            : Image.network(url, width: 30, height: 30, fit: BoxFit.cover),
        SizedBox(width: 10),
        Text(text, style: TextStyle(color: Colors.white, fontSize: 16)),
      ],
    ),
  );
}
