import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class ImageText extends StatelessWidget {
  final String url;
  final String text;
  final double space;

  const ImageText({super.key, required this.url, required this.text, this.space = 8.0});

  @override
  Widget build(BuildContext context) {
    final bool isSvg = url.toLowerCase().endsWith('.svg');
    return Padding(
      padding: EdgeInsets.symmetric(vertical: space),
      child: Row(
        children: <Widget>[
          isSvg
              ? SvgPicture.network(url, width: 30, height: 30, fit: BoxFit.cover)
              : Image.network(url, width: 30, height: 30, fit: BoxFit.cover),
          const SizedBox(width: 10),
          Text(text, style: const TextStyle(color: Colors.white, fontSize: 16)),
        ],
      ),
    );
  }
}
