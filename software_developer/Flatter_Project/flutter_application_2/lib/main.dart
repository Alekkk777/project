import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Widget per il nome dell'azienda
    const companyNameWidget = Text(
      'JECO PAVIA',
      style: TextStyle(color: Colors.red, fontSize: 20),
    );

    // Decorazione per il container del nome dell'azienda
    final companyNameDecoration = BoxDecoration(
      border: Border.all(color: Colors.blueAccent, width: 10),
    );

    // Margin per il container
    const myMargin = EdgeInsets.all(10);

    // Widget per la domanda
    const questionWidget = Text(
      'Come va?',
      style: TextStyle(fontSize: 16), // Aggiungi lo stile che preferisci qui
    );
    const thumb_up=Icon(Icons.thumb_up,
      color: Colors.blue,
      size: 100.0,);
    const thumb_down=Icon(Icons.thumb_down,
      color: Colors.blue,
      size: 100.0,);
    const thumbsWidget= Row(mainAxisAlignment: MainAxisAlignment.center,
                            children: [thumb_up,thumb_down]);

    return MaterialApp(
      home: Scaffold(
        body: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            // Container per il nome dell'azienda
            Container(
              margin: myMargin,
              decoration: companyNameDecoration,
              alignment: Alignment.center,
              child: companyNameWidget,
              height: 60, // Altezza adeguata per il container
            ),
            // Widget per la domanda
            questionWidget,
            thumbsWidget
          ],
        ),
      ),
    );
  }
}
